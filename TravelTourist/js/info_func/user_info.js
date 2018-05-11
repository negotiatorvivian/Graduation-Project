//change user information dialog
function show_dialog(){
	document.getElementById('book-form').style.display = 'block';
	var width = $('#occupation-select').width();
	$('#character-list').multiselect({
            buttonWidth: width
        });
	$('.btn-group').css('width',width);

}


function send_info(){
	var gender = $("#gender option:selected").val();
	var age = $("#age option:selected").text();
	var occupation = $("#occupation option:selected").val();
	var city = $("#city option:selected").val();
	var years = $("#years option:selected").val();
	var marital_status = $("#marital_status option:selected").val();
	var cur_user = {
		'gender' : gender,
		'age' : age,
		'occupation' : occupation,
		'city' : city,
		'years' : years,
		'marital_status' : marital_status
	};
	sessionStorage.setItem('cur_user', JSON.stringify(cur_user));
	// console.log(marital_status);
	address = 'http://127.0.0.1:8000/shopping_route/shopping/predict_result';
	var post_data = {
		"gender" : gender,
		"age" :age,
		"occupation" :occupation,
		'city':city,
		'years':years,
		'marital_status':marital_status,
	};

	var load_data = $.ajax({
		url : address,
		type : "POST",
		data : post_data,
		// async:false,
		dataType:"json",
		timeout : 30000,
		success : function(res){
			if (res.errorCode == 0){
				sessionStorage.setItem('rec_list', JSON.stringify(res.ret));
				window.location.href = 'index.html';
				return true;
			}
			else{
				alert('服务器旅游去了,待会再试试~');
				return false;
			}
		},
		fail : function(res){
			alert('服务器旅游去了,待会再试试~');
			return false;
		},
		complete : function(XMLHttpRequest,status){
	　　　　if(status=='timeout'){//超时,status还有success,error等值的情况
				// alert('服务器旅游去了,待会再试试~');
	 　　　　　 	load_data.abort();
				return false;
	　　　　}
　　}
	});
}