package states

import "strings"

var States = map[string]string {
    "WA": "Washington", "DE": "Delaware", "WI": "Wisconsin",
    "WV": "West Virginia", "HI": "Hawaii", "FL": "Florida",
    "WY": "Wyoming", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "TX": "Texas", "LA": "Louisiana",
    "NC": "North Carolina", "ND": "North Dakota", "NE": "Nebraska",
    "TN": "Tennessee", "NY": "New York", "PA": "Pennsylvania",
    "CA": "California", "NV": "Nevada", "VA": "Virginia", "CO": "Colorado",
    "AK": "Alaska", "AL": "Alabama", "AR": "Arkansas", "VT": "Vermont",
    "IL": "Illinois", "GA": "Georgia", "IN": "Indiana", "IA": "Iowa",
    "OK": "Oklahoma", "AZ": "Arizona", "ID": "Idaho", "CT": "Connecticut",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "OH": "Ohio",
    "UT": "Utah", "MO": "Missouri", "MN": "Minnesota", "MI": "Michigan",
    "RI": "Rhode Island", "KS": "Kansas", "MT": "Montana",
    "MS": "Mississippi", "SC": "South Carolina", "KY": "Kentucky",
    "OR": "Oregon", "SD": "South Dakota", "DC": "District of Columbia",
}

func AbbrevToName(abbrev string) (string, bool) {
    name, ok := States[strings.ToUpper(abbrev)]
    return name, ok
}

func NameToAbbrev(name string) (string, bool) {
    properName := strings.Title(strings.ToLower(name))

    for k, v := range States {
        if v == properName {
            return k, true
        }
    }

    return "", false
}

func Abbrevs() []string {
    abbrevs := make([]string, 0, len(States))

    for k := range States {
        abbrevs = append(abbrevs, k)
    }

    return abbrevs
}

func Names() []string {
    names := make([]string, 0, len(States))

    for _, v := range States {
        names = append(names, v)
    }

    return names
}
