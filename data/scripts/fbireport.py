import states
import cities
from xlrd import open_workbook
import os

REPORT_PATH = "../fbi/Table_8_Offenses_Known_to_Law_Enforcement_by_%s_by_City_2012.xls"

FIELDS = [
    "name", "population", "violent crime",
    "murder and nonnegligent manslaughter", "forcible rape",
    "robbery", "aggravated assault", "property crime",
    "burglary", "larceny-theft", "vehicle-theft", "arson"
]

CITY_NAME = 0

def findCity(city, reports):
    for row in range(5, reports.nrows):
        currentCity = reports.cell(row, CITY_NAME).value 

        if cities.cityNameEquals(city, currentCity):
            report = {}

            for col in range(1, reports.ncols):
                report[FIELDS[col]] = reports.cell(row, col).value
            
            return report

def loadCity(city, state):
    stateName = states.abbreviationToName(state)

    if not stateName:
        return

    try:
        stateName = stateName.replace(" ", "_")
        filename = REPORT_PATH % stateName

        workbook = open_workbook(filename)
        reports = workbook.sheets()[0]
        report = findCity(city, reports)
        
        if report:
            return report
    except:
        pass

    raise LookupError(city)

if __name__ == "__main__":
    print loadCity("Miami", "FL")
    print loadCity("Chicago", "IL")
