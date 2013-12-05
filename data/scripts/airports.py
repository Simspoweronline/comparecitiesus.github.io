import cities
import states

FILENAME = "../airports.csv"

def parseAirport(collumns):
    return {
        "airport": collumns[4].strip(),
        "ICAO": collumns[3].strip(),
        "IATA": collumns[2].strip(),
        "enplanements": int(collumns[6].replace(",", ""))
    }

def loadCity(city, state):
    currentState = ""
    airports = { "airports" : [] }

    for line in open(FILENAME):
        collumns = line.strip().split("\t")
        total = len(collumns)

        if total == 1:
            currentState = states.nameToAbbrevation(collumns[0])
        elif total == 7:
            if (currentState == state) and cities.cityNameEquals(city, collumns[0]):
                airports["airports"].append(parseAirport(collumns))
        else:
            print "ERROR:", collumns

    if not airports["airports"]:
        raise LookupError("No airport for %s" % city)

    return airports

if __name__ == "__main__":
    print loadCity("Orlando", "FL")
