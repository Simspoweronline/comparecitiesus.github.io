import urllib2
import json

def get_state_crime_report(state, filename):
  BASE_URL = "http://www.fbi.gov/about-us/cjis/ucr/crime-in-the-u.s/2012/crime-in-the-u.s.-2012/tables/8tabledatadecpdf/table-8-state-cuts/table_8_offenses_known_to_law_enforcement_by_%s_by_city_2012.xls/output.xls"

  encoded_state = state.lower().replace(" ", "_")
  state_url = BASE_URL % encoded_state

  try:
    xls_data = urllib2.urlopen(state_url).read()
  except:
    print "error downloading", state_url

  state_file = open(filename, "w")
  state_file.write(xls_data)
  state_file.close()


STATES = json.load(open("../states.json"))

for state in STATES.values():
  filename = "%s.xls" % state
  get_state_crime_report(state, filename)
