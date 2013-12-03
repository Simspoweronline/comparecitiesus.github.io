ABBREVIATION_TO_NAME = { 
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
    "OR": "Oregon", "SD": "South Dakota", "DC": "District of Columbia" 
}

NAME_TO_ABBREVIATION = { ABBREVIATION_TO_NAME.get(k): k for k in ABBREVIATION_TO_NAME } 

def abbreviationToName(abbreviation):
    return ABBREVIATION_TO_NAME.get(abbreviation)

def nameToAbbrevation(name):
    return NAME_TO_ABBREVIATION.get(name)

def getStatesByName():
    return NAME_TO_ABBREVIATION.keys() 

if __name__ == "__main__":
    print nameToAbbrevation("Florida")
    print abbreviationToName("FL")
    print getStatesByName()
