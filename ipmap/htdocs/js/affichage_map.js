jQuery.noConflict();



jQuery(

function create_ipmap(){
	var $ = jQuery;
	
	var string_marker = $("#marker_list").text();
	var array_marker = string_marker.split("!");
	var marker_len = array_marker.length;
	var list_marker = [];
	var i = 0;
	var obj = {};
	var tmp, tmp0,tmp1, tmp2, tmp3, tmp4;
	var map;
		   
	while (i < marker_len){
	    tmp0 = array_marker[i];
	    tmp = tmp0.split("?")
		tmp1 = tmp[0];
	    tmp2 = tmp[1];
	    tmp = tmp1.split(",");
	    tmp3 = tmp[0];
	    tmp4 = tmp[1];

	    obj = {latLng:[tmp3,tmp4], name:tmp2, cssClass: 'test'};
	    list_marker.push(obj);
	    i = i+1;
	}



	map = new jvm.Map({
		map: 'world_mill_en',
		panOnDrag: true,
		focusOn: {
		    x: 0.5,
		    y: 0.5,
		    scale: 1,
		    animate: true
		},
		markerStyle: {
		    initial: {
			fill: '#F8E23B',
			stroke: '#383f47'
		    }
		},
		backgroundColor: '#383f47',
		container: $('#map'),
		markers : list_marker
  
	    });


    });