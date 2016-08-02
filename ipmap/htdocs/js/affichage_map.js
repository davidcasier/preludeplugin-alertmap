
function create_ipmap(){

    var $ = jQuery;
   
    map = new jvm.Map({
	    map: 'world_mill_en',
	    panOnDrag: true,
	    markersSelectable: true,
	    focusOn: {
		x: 0.5,
		y: 0.5,
		scale: 0,
		animate: true
	    },
	    markerStyle: {
		initial: {
		    fill: '#F8E23B',
		    stroke: '#383f47'
		},
		selected: {
		    fill: '#33cc33',
		    stroke:'#000000',
		    "stroke-width": 2
		}
	    },
	    backgroundColor: '#383f47',
	    container: $("#map"),
	    markers : [],
	    series :{
		markers:[{
			attribute: 'r',
			scale: [3,15],
			values:[],
			min:1,
			max :20
		    },{
			attribute: 'fill',
			scale: ['#F8E23B','#DF0101'],
			values: [],
			min :1,
			max:20
		    }]
	    },
	    
	    onMarkerSelected: function(event,index, isSel,selectedMarkers){    
		
		if(isSel){
		    if(selectedMarkers.length ==1){
			$("div.alert_data:not(#"+index+")").hide(1000);
			$("#"+index).show(1000);
		    }
		    else{		   
			$("#"+index).show(1000);	   
		    }
		}
		else{
		     if(selectedMarkers.length ==0){
			 $("div.alert_data").show(1000);
		     }
		     else{
			 $("#"+index).hide(1000);	
		     }
		}
	    }
	});
}

