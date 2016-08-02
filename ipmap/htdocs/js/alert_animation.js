
function create_sortbuttons(){
    var $ = jQuery;
    var country_list = $("#country_list").text();
    country_list = country_list.replace("[","");
    country_list = country_list.replace("]","");
    country_list = country_list.replace(/\'/g,"");
    country_list = country_list.replace(/\n/g,"");
    country_list = country_list.replace(/ /g,"");
    var country_array = country_list.split(",");
    var x;
    var mapObj = $('#map').vectorMap('get', 'mapObject');

    for (x in country_array){
	document.getElementById(country_array[x]).addEventListener("click", function(event){
		var i = new String(this.id);
		event.preventDefault();
		$("div.alert_data:not("+"."+i+")").hide(1000);
		$("."+i).show(1000);
		mapObj.setFocus({region: i, animate: 1});
	    });
    }


    document.getElementById("All").addEventListener("click", function(event){
	    event.preventDefault();
	    $(".alert_data").show(1000);
	    mapObj.setFocus({scale: 0,lat:0.2,lng:0.41, animate: 1});
	});	    
}