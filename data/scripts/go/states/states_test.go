package states

import "testing"

func TestNameToAbbrv(t *testing.T) {
    testStates := map[string]string {
        "Florida": "FL",
        "CALIFORNIA": "CA",
        "new york": "NY",
    }

    for in, out := range testStates {
        name, ok := NameToAbbrev(in)

        if  name != out || !ok {
            t.Errorf("%v != %v", name, out)
        }
    }
}

func TestAbbrvToName(t *testing.T) {
    testStates := map[string]string {
        "fl": "Florida",
        "Ca": "California",
        "NY": "New York",
    }

    for in, out := range testStates {
        name, ok := AbbrevToName(in)

        if  name != out || !ok {
            t.Errorf("%v != %v", out, name)
        }
    }
}
