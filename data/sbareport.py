import cities
import states
import json
import urllib2

BASE_URL = "http://api.sba.gov/geodata/city_data_for_state_of/%s.json"
REPORT_PATH = "sba/%s.json"

def downloadStateReport(state, filename):
    stateUrl = BASE_URL % state
    report = json.load(urllib2.urlopen(stateUrl))
    stateFile = open(filename, "w")
    json.dump(report, stateFile)

def findCity(city, report):
    for currentCity in report:
        if cities.cityNameEquals(city, currentCity["name"]):
            return currentCity

def loadCity(city, state):
    try:
        filename = REPORT_PATH % state
        reports = json.load(open(filename))
        return findCity(city, reports)
    except IOError:
        raise LookupError(city)
        
if __name__ == "__main__":
    print loadCity("Miami", "FL")
    print loadCity("Chicago", "IL")
