import states
from xlrd import open_workbook
import re
import os

REPORT_PATH = "fbi/Table_8_Offenses_Known_to_Law_Enforcement_by_%s_by_City_2012.xls"

FIELDS = [
    "name", "population", "violent crime",
    "murder and nonnegligent manslaughter", "forcible rape",
    "robbery", "aggravated assault", "property crime",
    "burglary", "larceny-theft", "vehicle-theft", "arson"
]

CITY_NAME = 0

def sanitizeName(name):
    alphaOnly = re.sub("[^a-z]", "", name.lower())
    return alphaOnly

def cityNameEquals(city, otherCity):
    return sanitizeName(city) == sanitizeName(otherCity)
    
def loadCity(city, state):
    stateName = states.abbreviationToName(state)

    if not stateName:
        return

    stateName = stateName.replace(" ", "_")
    filename = REPORT_PATH % stateName

    workbook = open_workbook(filename)
    spreadsheet = workbook.sheets()[0]

    for row in range(5, spreadsheet.nrows):
        currentCity = spreadsheet.cell(row, CITY_NAME).value 

        if cityNameEquals(city, currentCity):
            report = {}

            for col in range(1, spreadsheet.ncols):
                report[FIELDS[col]] = spreadsheet.cell(row, col).value
            
            return report

if __name__ == "__main__":
    print loadCity("Miami", "FL")
    print loadCity("Miami", "FS")
    print loadCity("Chicago", "IL")
