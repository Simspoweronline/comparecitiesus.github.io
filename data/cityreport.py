import cities
import fbireport

def main():
    for currentCity in cities.MAJOR_CITIES:
        city = currentCity["name"]
        state = currentCity["state"]

        try:
            report = fbireport.loadCity(city, state)
        except LookupError:
            print city, state

if __name__ == "__main__":
  main()
