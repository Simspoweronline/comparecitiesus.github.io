import os
import urllib2 
import urllib
import json

BASE_URL = "http://api.sba.gov/geodata/all_links_for_city_of/%s/%s.json"
STATES = json.load(open("../states.json"))

def fetch_city_data(city, state):
  encoded_city = urllib.quote_plus(city)
  city_url = BASE_URL % (encoded_city, state)
  json_data = urllib2.urlopen(city_url).read()
  return json.loads(json_data)[0]

def get_abbrev(state_name):
  for k in STATES:
    if STATES[k] == state_name:
      return k

city_files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".json")]

for filename in city_files:
  city = json.load(open(filename))
  state = get_abbrev(city['state'])

  try:
    city_data = fetch_city_data(city['name'], state)
    city["url"] = city_data["url"]
    city["latitude"] = city_data["primary_latitude"]
    city["longitude"] = city_data["primary_longitude"]
    json.dump(city, open(filename, "w"))
  except:
    print "missing", city["name"]
