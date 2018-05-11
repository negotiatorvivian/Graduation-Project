default_info = {
	'category' : 18,
	'description' : 'Credit Cards,&nbsp;Appointment',
	'features' : 'Chicken,Awesome,Nugget',
	'score' : '4.5',
	'trade_name' : 'Street Food Cinema'
};
var information = 'Credit Cards, Appointment';
var time = '10:00-21:00';
function load_good_info(){
	var goods_list = sessionStorage.getItem('goods');
	if (goods_list == null){
		var rec_list1 = default_info;
	}
	else
		var rec_list1 = JSON.parse(goods_list);
	console.log(rec_list1);
	for(var i = 0; i < rec_list1.length; i++){
		ele_id = 'package' + i;
		var container = document.getElementById(ele_id);
		$(container).children("h4").first().text(rec_list1[i].trade_name);
		var count = parseInt(rec_list1[i].score);
		var str = '';
		for(var j = 0; j < count; j++){
			str += '★';
		}
		$(container).children("h5").first().text(str);
		$(container).children("img").first().attr('src', 'images/cat' + rec_list1[i].category + '.jpg');
		$(container).children("img").first().attr('alt', rec_list1[i].trade_name);
}
	
}

function get_concrete_info(i){
	var goods_list = sessionStorage.getItem('goods');
	if (goods_list == null){
		var rec_list1 = default_info;
	}
	else
		var rec_list1 = JSON.parse(goods_list);
	var container = document.getElementById('small-dialog');
	console.log(rec_list1[i].trade_name);
	$(container).children("h2").text(rec_list1[i].trade_name);
	var form = document.getElementById('dialog-form');
	var div_list = $(form).find('div');
	var attr_list = new Array();
	attr_list.push(rec_list1[i].trade_name);
	attr_list.push(rec_list1[i].description);
	attr_list.push(rec_list1[i].features);
	attr_list.push(rec_list1[i].score);
	attr_list.push(information);
	attr_list.push(time);

	for (item in div_list){
		if (item > attr_list.length - 1)
			break;
		$(div_list[item]).children('p').text(attr_list[item]);
	}
	return true;
}

function change_mode(){
	var root_ele = document.getElementById('small-dialog');
	var container = document.getElementById('dialog-form');
	container.style.display = 'none';
	var checkbox = document.getElementById('cat-select');
	checkbox.style.display = 'block';
	var name = $(root_ele).children("h2").text();
	$(root_ele).children("h2").text('Please choose the categories you like');
	sessionStorage.setItem('trade_name', name);
}

function get_option(){
	var container = document.getElementById('dialog-form');
	var checkbox = document.getElementById('cat-select');
	checkbox.style.display = 'none';
	container.style.display = 'block';
	var root_ele = document.getElementById('small-dialog');
	$(root_ele).children("h2").text(sessionStorage.getItem('trade_name'));
	var obj = document.getElementsByName('checkboxs');
	var prefer_cats = '';
	for(var i = 0; i < obj.length; i++){
		if(obj[i].checked)
			prefer_cats += obj[i].value + ',';
	}
	// console.log(prefer_cats);
	add_negative(prefer_cats);


}

function add_negative(prefer_cats){
	var res = sessionStorage.getItem('cur_user');
	var cur_user = JSON.parse(res);
	address = 'http://127.0.0.1:8000/shopping_route/shopping/modify_model';
	// var prefer_cats = 
	var post_data = {
		"gender" : cur_user.gender,
		"age" :cur_user.age,
		"occupation" :cur_user.occupation,
		'city':cur_user.city,
		'years':cur_user.years,
		'marital_status':cur_user.marital_status,
		'categories':prefer_cats
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
				return true;
			}
			else{
				return false;
			}
		},
		complete : function(XMLHttpRequest,status){
	　　　　if(status=='timeout'){//超时,status还有success,error等值的情况
	 　　　　　 	load_data.abort();
				return false;
	　　　　}
　　}
	});
	

}