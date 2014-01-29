import re
import calendar
import stations

MIN_FILE = "../climate/mly-tmin-normal.txt"
MAX_FILE = "../climate/mly-tmax-normal.txt"
min_stations = []
max_stations = []

def parseMonth(month):
  return calendar.month_name[int(month)]

def parseTemperature(temp):
  if temp == '-8888':
    return '    '

  return int(temp[:-1]) / 10.0

def printStation(station):
  print station["name"],
  print "\t".join(map(str, station["temps"]))

def parseStation(lines):
  station = {}

  stationName, months = parse_normal(lines)
  station["name"] = stationName
  station["temps"] = months

  return station

def parse_normal(line):
  blanks = re.compile(r"\s+")
  array = blanks.split(line.strip())

  stationName = array[0]
  months = map(parseTemperature, array[1:])

  return stationName, months

def parse_normal_file(filename):
  lines = open(filename).readlines()

  stations = {}

  for line in lines:
    station = parseStation(line)
    stations[station["name"]] = station

  return stations

def load_normals():
  global min_stations
  global max_stations

  min_stations = parse_normal_file(MIN_FILE)
  max_stations = parse_normal_file(MAX_FILE)

def getStationNormals(station_id):
  global min_stations

  if not min_stations:
    load_normals()

  mins = min_stations[station_id]
  maxs = max_stations[station_id]

  station = {}
  station["station"] = mins["name"]
  station["climate"] = zip(mins["temps"], maxs["temps"])
  return station

def loadCity(city):
  stations_near = stations.near(float(city["primary_latitude"]), float(city["primary_longitude"]))

  if not stations_near:
    raise LookupError("No stations near %s" % (city["name"], city["state"]))

  temperature = getStationNormals(stations_near[0])
  return temperature

if __name__ == "__main__":
  city = {
    "state": "FL", 
    "name": "Gainesville", 
    "primary_latitude": "29.65", 
    "primary_longitude": "-82.32"
  }

  print loadCity(city)
