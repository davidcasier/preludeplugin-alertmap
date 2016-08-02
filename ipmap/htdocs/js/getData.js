 
function add_map_data(){
    
    $.get('ipmap/txt/alrt.txt', function(data) {

	    var array_marker = data.split("\n");
	    var marker_len = array_marker.length;
	    var list_marker = [];
	    var list_series_value = [];
	    var i = 0;
	    var obj = {};
	    var tmp, tmp0,tmp1, tmp2, tmp3, tmp4;
	    var mapObj = $("#map").vectorMap('get','mapObject');

	    while (i < marker_len){
		tmp0 = array_marker[i];
		tmp = tmp0.split("?");
		tmp1 = tmp[0];
		tmp2 = tmp[1];
		if(tmp[2]){
		    list_series_value.push(tmp[2]);
		}
		tmp = tmp1.split(",");
		tmp3 = tmp[0];
		tmp4 = tmp[1];
		alert("nb:"+i+" "+tmp3+", "+tmp4+"\n Name"+tmp2);
		if(tmp3){
		obj = {latLng:[tmp3,tmp4], name:tmp2};
		}
		list_marker.push(obj);
		i = i+1;
	    }
	    
	    alert(list_marker.length);
	    alert(list_series_value.length)
	    
	    mapObj.addMarkers(list_marker,[]);
	    mapObj.series.markers[0].setValues(list_series_value);
	    mapObj.series.markers[1].setValues(list_series_value);

	},'text');
}