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