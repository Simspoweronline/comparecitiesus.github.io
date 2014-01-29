import math

STATIONS_FILE = "../climate/stations.txt"
MAX_DISTANCE_IN_KM = 20
stations = []

def parse_station(line):
  return { 
      "id": line[:12].strip(),
      "latitude": float(line[12:21]),
      "longitude": float(line[21:31]),
      "elevation": float(line[31:38]),
      "state": line[38:41],
      "name": line[41:72]
  }

def distance(city_lat, city_long, station_lat, station_long):
  EARTH_RADIUS = 6371
  delta_lat = deg2rad(station_lat - city_lat)
  delta_long = deg2rad(station_long - city_long)
  a = (math.sin(delta_lat / 2) * math.sin(delta_lat / 2) +
       math.cos(deg2rad(city_lat)) * math.cos(deg2rad(station_lat)) *
       math.sin(delta_long / 2) * math.sin(delta_long / 2))

  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  return EARTH_RADIUS * c

def deg2rad(deg):
  return deg * (math.pi / 180)

def load_stations():
  lines = open(STATIONS_FILE).readlines()
  return map(parse_station, lines)

def near(latitude, longitude):
  global stations

  if not stations:
    stations = load_stations()

  stations_near = []

  for s in stations:
    station_distance = distance(latitude, longitude, s["latitude"], s["longitude"])
    if station_distance < MAX_DISTANCE_IN_KM:
      stations_near.append(s["id"])

  return stations_near

