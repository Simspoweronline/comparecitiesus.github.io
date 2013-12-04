import json 
import re

CITIES_FILENAME = "../cities/majorcities.json"
MAJOR_CITIES = json.load(open(CITIES_FILENAME))

def sanitizeName(name):
    name = name.lower().replace("st.", "saint")
    alphaOnly = re.sub("[^a-z]", "", name)
    return alphaOnly

def cityNameEquals(city, otherCity):
    return sanitizeName(otherCity).startswith(sanitizeName(city))
