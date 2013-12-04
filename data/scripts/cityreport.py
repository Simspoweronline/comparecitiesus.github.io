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
            fbi = fbireport.loadCity(city, state) 
            report.update((k, v) for k, v in fbi.iteritems() if v is not None)
        except LookupError:
            print city, state

        try:
            sba = sbareport.loadCity(city, state)
            report.update((k, v) for k, v in sba.iteritems() if v is not None)
        except LookupError:
            print city, state

        if report:
            report["id"] = currentCity["id"]
            report["name"] = city
            report["state"] = state
            report["full_name"] = "%s, %s" % (city, state) 
            filename = REPORT_PATH % report["id"]
            cityFile = open(filename, "w")
            json.dump(report, cityFile)

if __name__ == "__main__":
    generateAll()
