import json 
import re

CITIES_FILENAME = "majorcities.json"
MAJOR_CITIES = json.load(open(CITIES_FILENAME))

def sanitizeName(name):
    alphaOnly = re.sub("[^a-z]", "", name.lower())
    return alphaOnly

def cityNameEquals(city, otherCity):
    return sanitizeName(otherCity).startswith(sanitizeName(city))
