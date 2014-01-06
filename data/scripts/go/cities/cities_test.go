package cities

import "testing"

func TestSanitizeName(t *testing.T) {
    cityNames := map[string]string {
        "St. pAuL-PETER": "stpaulpeter",
        "MIAMI": "miami",
        "-''abc--..saint": "abcsaint",
    }

    for in, out := range cityNames {
        if sanitized := SanitizeName(in); sanitized != out {
            t.Errorf("%v != %v", sanitized, out)
        }
    }
}

func TestNameLike(t *testing.T) {
    cityNames := map[string]string {
        "Miami": "Miami",
        "Saint Peter": "st. peter",
        "ho-ho ha-ha": "HoHoHaHa",
        "New York": "New York City",
    }

    for city, otherCity := range cityNames {
        if !NameLike(city, otherCity) {
            t.Errorf("%v != %v", city, otherCity)
        }
    }
}

func TestMajorCities(t *testing.T) {
    if cities := MajorCities(); len(cities) < 299 {
        t.Errorf("%+v %d", cities, len(cities))
    }
}
