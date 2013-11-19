$(function() {
  function getParameterByName( name,href ) {
    name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
    var regexS = "[\\?&]"+name+"=([^&#]*)";
    var regex = new RegExp( regexS );
    var results = regex.exec( href );

    if( results == null )
      return "";
    else
      return decodeURIComponent(results[1].replace(/\+/g, " "));
  }

  function fetchCityData(cityId, tag) {
    var cityUrl = "data/cities/" + cityId + ".json";

    $.getJSON(cityUrl, function(data) {
      $('<pre>' + data['name'] + ", " + data['state'] + "\nPopulation: " + data["population"] + '</pre>').appendTo(tag);
    });  
  }

  var cities = getParameterByName("compare", document.URL).split(",");
  
  for (var i = 0; i < cities.length; i++) {
    fetchCityData(cities[i], "#city" + (i + 1));
  }
});
