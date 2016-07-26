function newMarker(lat,lng,MarkerName){
        $('#map1').addMarker(0,{latLng: [lat,lng], name: MarkerName});
}