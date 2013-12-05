import cities
import states
import json
import urllib2

BASE_URL = "http://api.sba.gov/geodata/city_data_for_state_of/%s.json"
REPORT_PATH = "../sba/%s.json"

FIELDS = [
    u'link_title', u'description', u'fips_class', u'url', 
    u'feature_id', u'state_name', u'fips_county_cd', 
    u'state_abbreviation', u'full_county_name', u'county_name', 
    u'feat_class', u'primary_latitude', u'primary_longitude', u'name']

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
        report = findCity(city, reports)

        if report:
            return report

    except IOError:
        pass

    raise LookupError(city)
        
if __name__ == "__main__":
    print loadCity("Miami", "FL").keys()
