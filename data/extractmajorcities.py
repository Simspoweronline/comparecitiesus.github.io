import json
import re

CITY_FILENAME = "cities.json"
STATE_DATA_FOLDER = "fbi"

def load_fbi_state_stats(state):
  state_filename = "%s/%s.json" % (STATE_DATA_FOLDER, state)
  state_file = open(state_filename)
  return json.load(state_file)

def extract_city(city_name, state_data):
  target_city_token = sanitize_name(city_name)

  for current_city in state_data:
    current_city_token = sanitize_name(current_city['name'])

    if current_city_token.startswith(target_city_token):
      return current_city

def sanitize_name(city_name):
  name_without_punctuation = re.sub("[.\'\"]", "", city_name.lower())
  return re.sub("[- ]", "_", name_without_punctuation)

def generate_city_id(city, state):
  city_token = sanitize_name(city)
  state_token = sanitize_name(state)

  city_id = "%s_%s" % (city_token, state_token)
  return city_id

def load_city(city_name, state):
  city_id = generate_city_id(city_name, state)
  state_data = load_fbi_state_stats(state)

  city = extract_city(city_name, state_data)

  if city:
    city["id"] = city_id
  else:
    raise Exception("City not found: %s" % city_name)

  return city

def save_city(city):
  try:
    city_id = city["id"]
    city_filename = "cities/%s.json" % city_id
    city_file = open(city_filename, "w")
    json.dump(city, city_file)
    city_file.close()
  except IOError:
    print "Unable to create file for", city_id

def load_major_cities():
  cities_file = open(CITY_FILENAME)
  cities_json = json.load(cities_file)
  cities_file.close()

  return cities_json

def main():
  major_cities = load_major_cities()

  for current_city in major_cities:
    city_name = current_city['current_city']
    state = current_city['state']

    try:
      city = load_city(city_name, state)
      save_city(city)
    except:
      print "No data for %s, %s" % (city_name, state)

if __name__ == "__main__":
  main()
