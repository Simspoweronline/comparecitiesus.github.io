package cities

import (
    "strings"
    "regexp"
    "encoding/json"
    "io/ioutil"
)

const CITIES_FILENAME = "/home/paulo/comparecitiesus.github.io/data/cities/majorcities.json"
const NOT_LOWERCASE = "[^a-z]"

func SanitizeName(name string) string {
    expanded := strings.Replace(name, "st.", "saint", -1)
    re := regexp.MustCompile(NOT_LOWERCASE)
    return re.ReplaceAllString(strings.ToLower(expanded), "")
}

func NameLike(a, b string) bool {
    first, second := SanitizeName(a), SanitizeName(b)

    if len(second) > len(first) {
        first, second = second, first
    }

    return strings.HasPrefix(first, second)
}

type City struct {
    Name string
    State string
}

func MajorCities() []City {
     jsonBlob, err := ioutil.ReadFile(CITIES_FILENAME)

     if err != nil {
        panic(err)
     }

    var cities []City
    err = json.Unmarshal(jsonBlob, &cities)

    if err != nil {
        panic(err)
    }

    return cities
}
