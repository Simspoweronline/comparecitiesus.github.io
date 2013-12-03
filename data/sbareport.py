import states
import json
import urllib2

BASE_URL = "http://api.sba.gov/geodata/city_data_for_state_of/%s.json"
SBA_PATH = "sba/%s.json"

def downloadStateReport(state, filename):
    stateUrl = BASE_URL % state
    report = json.load(urllib2.urlopen(stateUrl))
    stateFile = open(filename, "w")
    json.dump(report, stateFile)

if __name__ == "__main__":
    for state in states.getStates():
        print state
        filename = SBA_PATH % state
        downloadStateReport(state, filename)
