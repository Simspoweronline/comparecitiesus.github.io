import cities
import fbireport
import sbareport
import json

REPORT_PATH = "../cities/%s.json"

def generateAll():
    for currentCity in cities.MAJOR_CITIES:
        city = currentCity["name"]
        state = currentCity["state"]

        report = {}

        try:
            report.update(fbireport.loadCity(city, state))
        except LookupError:
            print city, state

        try:
            report.update(sbareport.loadCity(city, state))
        except LookupError:
            print city, state

        if report:
            report["id"] = currentCity["id"]
            filename = REPORT_PATH % report["id"]
            cityFile = open(filename, "w")
            json.dump(report, cityFile)

if __name__ == "__main__":
    generateAll()
