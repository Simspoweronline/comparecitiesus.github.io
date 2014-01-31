import re
import calendar

def parseMonth(month):
  return calendar.month_name[int(month)]

def parseTemperature(temp):
  if temp == '-8888':
    return '    '

  return int(temp[:-1]) / 10.0

def printStation(station):
  print station["name"]

  for month in range(1, 13):
    print parseMonth(month) + "\t", 
    print "\t".join(map(str, station[month]))

def parseStation(lines):
  station = {}

  for line in lines:
    stationName, month, days =  parseLine(line)
    station["name"] = stationName
    station[month] = days

  return station

def parseLine(line):
  blanks = re.compile(r"\s+")
  array = blanks.split(line.strip())

  stationName = array[0]
  month = int(array[1])
  days = map(parseTemperature, array[2:])

  return stationName, month, days

def parseNormalFile(filename):
  lines = open(filename).readlines()
  totalLines = len(lines)

  stations = {}

  for start in range(0, totalLines, 12):
    months = lines[start: start + 12]
    station = parseStation(months)
    stations[station["name"]] = station

  return stations

if __name__ == "__main__":
  filename = "dly-tmin-normal.txt"
  stations = parseNormalFile(filename)
  printStation(stations["USC00083322"])
