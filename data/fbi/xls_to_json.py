from xlrd import open_workbook
import json
import os

xls_files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".xls")]

field_name = ["name", "population", "violent crime",
    "murder and nonnegligent manslaughter", "forcible rape",
    "robbery", "aggravated assault", "property crime",
    "burglary", "larceny-theft", "vehicle-theft", "arson"]

for filename in xls_files:
  state = filename.replace(".xls", "")
  wb = open_workbook(filename)
  spreadsheet = wb.sheets()[0]

  cities = []
  
  for row in range(5, spreadsheet.nrows):
    city = {}
    city["state"] = state 

    for col in range(spreadsheet.ncols):
      city[field_name[col]] = spreadsheet.cell(row, col).value

    cities.append(city)
  
  json_file = open("%s.json" % state, "w") 
  json.dump(cities, json_file)
  json_file.close()
