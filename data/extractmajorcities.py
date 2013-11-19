import json
import re

def sanitize_name(city_name):
  alpha_only = re.sub("[.\'\"]", "", city_name.lower())
  city_id = re.sub("[- ]", "_", alpha_only)
  return city_id

def generate_city_id(city, state):
  city_token = sanitize_name(city)
  state_token = sanitize_name(state)
  city_id = "%s_%s" % (city_token, state_token)
  return city_id

def load_state_data(state):
  STATE_DATA_FOLDER = "fbi"
  state_filename = "%s/%s.json" % (STATE_DATA_FOLDER, state)

  try:
    state_file = open(state_filename)
  except IOError:
    return None

  return json.load(state_file)

def extract_city(city_name, state_data):
  target_city_token = sanitize_name(city_name)

  for city in state_data:
    current_city_token = sanitize_name(city['name'])

    if current_city_token.startswith(target_city_token):
      return city

  return None

def load_city_data(city_name, state):
  city_id = generate_city_id(city_name, state)
  state_data = load_state_data(state)

  if not state_data:
    return None

  city_data = extract_city(city_name, state_data)

  if city_data:
    city_data["id"] = city_id

  return city_data

def create_city_file(city_data):
  try:
    city_id = city_data['id']
    city_filename = "cities/%s.json" % city_id
    city_file = open(city_filename, "w")
    json.dump(city_data, city_file)
    city_file.close()
  except IOError:
    print "Unable to create file for", city_id

if __name__ == "__main__":
  CITY_FILENAME = "cities.json"

  cities_file = open(CITY_FILENAME)
  cities_json = json.load(cities_file)

  for city in cities_json:
    city_name = city['city']
    state = city['state']

    city_data = load_city_data(city_name, state)

    if city_data:
      create_city_file(city_data)
    else:
      print "No data for %s, %s" % (city_name, state)
