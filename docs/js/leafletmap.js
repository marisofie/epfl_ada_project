//This class can be deleted must likely. 

window.onload = function () {
    var basemap = L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
	});

  $.getJSON("/maps/Boundaries-ZIPCodes.geojson", function(data) {
    var geojson = L.geoJSON(data, {
      onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.zip);
      }
  });
  
    var map = L.map('map')
    .fitBounds(geojson.getBounds());

    basemap.addTo(map);
    geojson.addTo(map);
  });

};

