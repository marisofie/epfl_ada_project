window.onload = function () {
    var basemap = L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
	});

  $("#map").ready(function() {
    $.getJSON("/maps/Boundaries-ZIPCodes.geojson", function(data) {
      var geojson = L.geoJson(data, {
        onEachFeature: function (feature, layer) {
          layer.bindPopup(feature.properties.Area_Name);
        }
      });
  });
  


    var map = L.map('map')
    .fitBounds(geojson.getBounds());

    basemap.addTo(map);
    geojson.addTo(map);
  });

};

