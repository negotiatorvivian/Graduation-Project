/* Close */
$(document).ready(function(){
  $(".panel-tools .closed-tool").click(function(event){
  $(this).parents(".book-form").fadeToggle(400);
  return false;
	}); 
});

/* Window resize */
$(window).resize(function(){
	var width = $('#occupation-select').width();
	$('.btn-group').css('width',width);
});




function updateLocation(location){
	// var cur_lat = location.coords.latitude.toFixed(5);
	// var cur_lon = location.coords.longitude.toFixed(5);
	var cur_lat = location.coords.latitude;
	var cur_lon = location.coords.longitude;
	console.log(cur_lat);
	sessionStorage.setItem('cur_lat', cur_lat);
    sessionStorage.setItem('cur_lon', cur_lon);
}

function handleLocationError(error){
	if (error.code == 0){
        alert("Unknown Error.");  
	}
	else if(error.code == 1){
		alert("We are not allowed to get your location!");  
	}
	else if(error.code == 2){
		alert("Can't get your location. Wait and try again.");  
	}
	else{
		alert("Time out. Check your internet");  
	}

}

$(document).ready(function(){
	var d = new Date();
	var datepicker = $("#datepicker");
	var input_list = $(datepicker).find("input");
	$(input_list[0]).attr('value', d.getFullYear());
	$(input_list[1]).attr('value', d.getMonth() + 1);
	$(input_list[2]).attr('value', d.getDate());
	$(input_list[3]).attr('value', d.getHours());
	$(input_list[4]).attr('value', d.getMinutes());
	var width = $(input_list[4]).width();
	var width1 = $(datepicker).width();
	var width2 = (width1 - 5 * width) / 2;
	$(datepicker).css('padding-left', 'width2');

});

$(document).ready(function(){
	var height = $(window).height() - 45;
	$('#packages').css('min-height', height);
})

$(document).ready(function(){
	var height = $(window).height() - 33;
	$('#home1').css('min-height', height);
	console.log(height);
	$('.slides-box').css('min-height', height);
	$('.pictures').css('height', height);
})
