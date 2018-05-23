// var directionsService = new google.maps.DirectionsService();
var map;
var distances = new Array();
var directionsDisplay;
var styles = {
        default: null,
        silver: [
          {
            elementType: 'geometry',
            stylers: [{color: '#f5f5f5'}]
          },
          {
            elementType: 'labels.icon',
            stylers: [{visibility: 'off'}]
          },
          {
            elementType: 'labels.text.fill',
            stylers: [{color: '#616161'}]
          },
          {
            elementType: 'labels.text.stroke',
            stylers: [{color: '#f5f5f5'}]
          },
          {
            featureType: 'administrative.land_parcel',
            elementType: 'labels.text.fill',
            stylers: [{color: '#bdbdbd'}]
          },
          {
            featureType: 'poi',
            elementType: 'geometry',
            stylers: [{color: '#eeeeee'}]
          },
          {
            featureType: 'poi',
            elementType: 'labels.text.fill',
            stylers: [{color: '#757575'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'geometry',
            stylers: [{color: '#e5e5e5'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          },
          {
            featureType: 'road',
            elementType: 'geometry',
            stylers: [{color: '#ffffff'}]
          },
          {
            featureType: 'road.arterial',
            elementType: 'labels.text.fill',
            stylers: [{color: '#757575'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry',
            stylers: [{color: '#dadada'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'labels.text.fill',
            stylers: [{color: '#616161'}]
          },
          {
            featureType: 'road.local',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          },
          {
            featureType: 'transit.line',
            elementType: 'geometry',
            stylers: [{color: '#e5e5e5'}]
          },
          {
            featureType: 'transit.station',
            elementType: 'geometry',
            stylers: [{color: '#eeeeee'}]
          },
          {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [{color: '#c9c9c9'}]
          },
          {
            featureType: 'water',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9e9e9e'}]
          }
        ],

        night: [
          {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
          {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
          {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
          {
            featureType: 'administrative.locality',
            elementType: 'labels.text.fill',
            stylers: [{color: '#d59563'}]
          },
          {
            featureType: 'poi',
            elementType: 'labels.text.fill',
            stylers: [{color: '#d59563'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'geometry',
            stylers: [{color: '#263c3f'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'labels.text.fill',
            stylers: [{color: '#6b9a76'}]
          },
          {
            featureType: 'road',
            elementType: 'geometry',
            stylers: [{color: '#38414e'}]
          },
          {
            featureType: 'road',
            elementType: 'geometry.stroke',
            stylers: [{color: '#212a37'}]
          },
          {
            featureType: 'road',
            elementType: 'labels.text.fill',
            stylers: [{color: '#9ca5b3'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry',
            stylers: [{color: '#746855'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry.stroke',
            stylers: [{color: '#1f2835'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'labels.text.fill',
            stylers: [{color: '#f3d19c'}]
          },
          {
            featureType: 'transit',
            elementType: 'geometry',
            stylers: [{color: '#2f3948'}]
          },
          {
            featureType: 'transit.station',
            elementType: 'labels.text.fill',
            stylers: [{color: '#d59563'}]
          },
          {
            featureType: 'water',
            elementType: 'geometry',
            stylers: [{color: '#17263c'}]
          },
          {
            featureType: 'water',
            elementType: 'labels.text.fill',
            stylers: [{color: '#515c6d'}]
          },
          {
            featureType: 'water',
            elementType: 'labels.text.stroke',
            stylers: [{color: '#17263c'}]
          }
        ],

        retro: [
          {elementType: 'geometry', stylers: [{color: '#ebe3cd'}]},
          {elementType: 'labels.text.fill', stylers: [{color: '#523735'}]},
          {elementType: 'labels.text.stroke', stylers: [{color: '#f5f1e6'}]},
          {
            featureType: 'administrative',
            elementType: 'geometry.stroke',
            stylers: [{color: '#c9b2a6'}]
          },
          {
            featureType: 'administrative.land_parcel',
            elementType: 'geometry.stroke',
            stylers: [{color: '#dcd2be'}]
          },
          {
            featureType: 'administrative.land_parcel',
            elementType: 'labels.text.fill',
            stylers: [{color: '#ae9e90'}]
          },
          {
            featureType: 'landscape.natural',
            elementType: 'geometry',
            stylers: [{color: '#dfd2ae'}]
          },
          {
            featureType: 'poi',
            elementType: 'geometry',
            stylers: [{color: '#dfd2ae'}]
          },
          {
            featureType: 'poi',
            elementType: 'labels.text.fill',
            stylers: [{color: '#93817c'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'geometry.fill',
            stylers: [{color: '#a5b076'}]
          },
          {
            featureType: 'poi.park',
            elementType: 'labels.text.fill',
            stylers: [{color: '#447530'}]
          },
          {
            featureType: 'road',
            elementType: 'geometry',
            stylers: [{color: '#f5f1e6'}]
          },
          {
            featureType: 'road.arterial',
            elementType: 'geometry',
            stylers: [{color: '#fdfcf8'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry',
            stylers: [{color: '#f8c967'}]
          },
          {
            featureType: 'road.highway',
            elementType: 'geometry.stroke',
            stylers: [{color: '#e9bc62'}]
          },
          {
            featureType: 'road.highway.controlled_access',
            elementType: 'geometry',
            stylers: [{color: '#e98d58'}]
          },
          {
            featureType: 'road.highway.controlled_access',
            elementType: 'geometry.stroke',
            stylers: [{color: '#db8555'}]
          },
          {
            featureType: 'road.local',
            elementType: 'labels.text.fill',
            stylers: [{color: '#806b63'}]
          },
          {
            featureType: 'transit.line',
            elementType: 'geometry',
            stylers: [{color: '#dfd2ae'}]
          },
          {
            featureType: 'transit.line',
            elementType: 'labels.text.fill',
            stylers: [{color: '#8f7d77'}]
          },
          {
            featureType: 'transit.line',
            elementType: 'labels.text.stroke',
            stylers: [{color: '#ebe3cd'}]
          },
          {
            featureType: 'transit.station',
            elementType: 'geometry',
            stylers: [{color: '#dfd2ae'}]
          },
          {
            featureType: 'water',
            elementType: 'geometry.fill',
            stylers: [{color: '#b9d3c2'}]
          },
          {
            featureType: 'water',
            elementType: 'labels.text.fill',
            stylers: [{color: '#92998d'}]
          }
        ],

        hiding: [
          {
            featureType: 'poi.business',
            stylers: [{visibility: 'off'}]
          },
          {
            featureType: 'transit',
            elementType: 'labels.icon',
            stylers: [{visibility: 'off'}]
          }
        ]
      };

function mark_destination(){
    if(sessionStorage.getItem('points') == null){
        alert('请先选择您的目的地~');
        return false;
    }
     
    document.getElementById('route').style.display = 'block';
    document.getElementById('map').style.display = 'block';
    if(document.getElementById('map') == null)
      return false;
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'http://maps.googleapis.com/maps/api/js?key=AIzaSyCxxGVTHObFEHv7WGjbFiiR-3SEm4PAahE&callback=initMap';
    document.body.appendChild(script);
}

// map api initial
function initMap() {
    var index = 0;
    do{
      var cur_lat = new Number(sessionStorage.getItem('cur_lat'));
      var cur_lon = new Number(sessionStorage.getItem('cur_lon'));
      if (cur_lat == null)
          setTimeout("pause()",1000);
          index = index + 1;
      }
    while(cur_lat == null && index < 5);
    var cur_location = {lat:cur_lat.valueOf(), lng:cur_lon.valueOf()};
    directionsDisplay = new google.maps.DirectionsRenderer();

    var map = new google.maps.Map(document.getElementById('map'), {
      center: cur_location,
      zoom: 13,
      mapTypeControl: false
    });
    var trafficLayer = new google.maps.TrafficLayer();
    trafficLayer.setMap(map);
    var marker = new google.maps.Marker({
      position: cur_location,
      map: map
    });	

    var styleControl = document.getElementById('style-selector-control');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(styleControl);

    var styleSelector = document.getElementById('style-selector');
    map.setOptions({styles: styles[styleSelector.value]});

    styleSelector.addEventListener('change', function() {
      map.setOptions({styles: styles[styleSelector.value]});
    });	
    google.maps.event.addListener(marker, 'click', function() {
      map.setZoom(9);
      map.setCenter(marker.getPosition());
    });
    directionsDisplay.setMap(map);

    var res = sessionStorage.getItem('points');
    var destinations = JSON.parse(res);

    var res = sessionStorage.getItem('trade_names');
    var names = JSON.parse(res);

    for(var i in destinations){
      var lat = new Number(destinations[i].latitude);
      var lon = new Number(destinations[i].longitude);
      var cur_location = {lat:lat.valueOf(), lng:lon.valueOf()};
      var marker = new google.maps.Marker({
        position: cur_location,
        map: map
      }); 
      var res = cal_distance(cur_lat, cur_lon, lat, lon);
      distances.push(res);
    }
    var eles = $('.topstats').find('li');
    for(var i in eles){
        var labels = document.getElementById('destination' + i);
        labels.style.display = 'block';
        if(names[i] == null){
          labels.style.display = 'none';
        }
        $(labels).children("h3").text(names[i]);
        $(labels).find("b").text(distances[i] + ' km');
    }
    }



function cal_distance(lat1, lng1, lat2, lng2) {
    var radLat1 = lat1 * Math.PI / 180.0;
    var radLat2 = lat2 * Math.PI / 180.0;
    var a = radLat1 - radLat2;
    var b = lng1 * Math.PI / 180.0 - lng2 * Math.PI / 180.0;
    var s = 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(a / 2), 2) + Math.cos(radLat1) * Math.cos(radLat2) * Math.pow(Math.sin(b / 2), 2)));
    s = s * 6378.137;
    s = Math.round(s * 10000) / 10000;
    return s
};


function calcRoute(start, destination, waypoints, time){
  var start = start;
  var end = destination;
  var request = {
    origin: start,
    destination: destination,
    travelMode: 'DRIVING',
    // 'travelMode': 'TRANSIT',
    // 'transitOptions': TransitOptions,
    drivingOptions: {
      departureTime: new Date(time),
        trafficModel: 'pessimistic'
    },
    // unitSystem: UnitSystem.METRIC,
    waypoints: waypoints,
    optimizeWaypoints: true,
    provideRouteAlternatives: true,
    // 'avoidHighways': Boolean,
    // 'avoidTolls': Boolean,
    region: 'CN'
  };
  var directionsService = new google.maps.DirectionsService();

  directionsService.route(request, function(response, status) {
    if (status == 'OK') {
        directionsDisplay.setDirections(response);
        var route = response.routes[0];
        var summaryPanel = document.getElementById('directions-panel');
        summaryPanel.innerHTML = '';
      // For each route, display summary information.
        for (var i = 0; i < route.legs.length; i++) {
            var routeSegment = i + 1;
            summaryPanel.innerHTML += '<i class="fa fa-paper-plane-o" aria-hidden="true" style="color:#f3a448;"></i>&nbsp;&nbsp;' + route.legs[i].distance.text + '<br>';
            summaryPanel.innerHTML += '<i class="fa fa-circle-o" aria-hidden="true" style="color:#2c925e;"></i>&nbsp;&nbsp;' + route.legs[i].start_address + '<br>';
            summaryPanel.innerHTML += '<span class="fa fa-circle-o" aria-hidden="true" style="color:#db3552;"></span>&nbsp;&nbsp;' + route.legs[i].end_address + '<br><br>';
            // summaryPanel.innerHTML += route.legs[i].distance.text + '<br><br>';
      }
    }
    else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}


function route_design(time){
    var cur_lat = new Number(sessionStorage.getItem('cur_lat'));
    var cur_lon = new Number(sessionStorage.getItem('cur_lon'));
    var start = {lat:cur_lat.valueOf(), lng:cur_lon.valueOf()};

    var res = sessionStorage.getItem('points');
    var destinations = JSON.parse(res);
    var waypoints = new Array();
    for(var i in destinations){
      // var waypoint = new google.maps.LatLng(destinations[i].latitude.valueOf(), destinations[i].longitude.valueOf());
        var lat = (destinations[i].latitude);
        var lng = (destinations[i].longitude);
        var waypoint = new google.maps.LatLng(lat, lng);
        var arg = {
          location : waypoint,
          stopover : true
        };
        waypoints.push(arg);
    }
    var destination = waypoints.pop().location;
    var d = Date.UTC(2018,5,24,7,0,0);
    calcRoute(start, destination, waypoints, d);

}

