jQuery.noConflict();

jQuery(

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

	//alert(typeof country_array[0]);

	$(document).on("ready" ,function(){
		//alert('ce code est executé');
		for (x in country_array){
		    //alert(country_array[x]);
		    document.getElementById(country_array[x]).addEventListener("click", function(event){
			    var i = new String(this.id);
			    event.preventDefault();
			    $("div.alert_data:not("+"."+i+")").hide(1000);
			    $("."+i).show(1000);
			});
		}


		document.getElementById("All").addEventListener("click", function(event){
			event.preventDefault();
			$(".alert_data").show(1000);
		    });
	    });
    });