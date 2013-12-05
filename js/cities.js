$(document).ready(function() {
    function addCommas(nStr) {
        nStr += '';
        x = nStr.split('.');
        x1 = x[0];
        x2 = x.length > 1 ? '.' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;

        while (rgx.test(x1)) {
            x1 = x1.replace(rgx, '$1' + ',' + '$2');
        }

        return x1 + x2;
    }

    function fetchCityData(cityId) {
        var cityUrl = "data/cities/" + cityId + ".json";

        $.getJSON(cityUrl, function(data) {
            $("#cities").show();

            var ids = ["city-name", "city-website", "county-name", "city-population", "airport", "city-violent-crime",
            "city-rape", "city-murders", "city-robbery", 
            "city-vehicle-theft"];

            var fields = ["full_name", "url", "county_name", "population", "airports", "violent crime", 
            "forcible rape", "murder and nonnegligent manslaughter",
            "robbery", "vehicle-theft"];

            for (var i = 0; i < fields.length; i++) {
                var property = fields[i];
                var value = data[property]

                if (value === undefined) {
                    value = "";
                }
                if (typeof value === "number") {
                    value = addCommas(value);
                }
                else if(property == "url" && value) {
                    value = "<a href='" +  value  + "'>" + value + "</a>";
                }
                else if(property == "airports" && value) {
                    value = value[0]["airport"] + " (" + value[0]["IATA"]+ ")"  
                }

                var el = "<td class='" + data.id + "'>" + value + "</td>;"
                $(el).appendTo("#" + ids[i]);
            }
        });  
    };

    function addCity(city) {
        fetchCityData(city.id);
    };

    function deleteCity(city) {
        $("." + city.id).remove(); 
    };

    $.getJSON("data/cities/majorcities.json", function(cities) {
        options = { 
            hintText: "Type in a city", 
            animateDropdown: false,
            searchDelay: 100,
            tokenLimit: 4,
            resultsLimit: 5,
            preventDuplicates: true,
            propertyToSearch: "display",
            onAdd: addCity,
            onDelete: deleteCity,
        };

        $("#searchbar").tokenInput(cities, options);
    });
});
