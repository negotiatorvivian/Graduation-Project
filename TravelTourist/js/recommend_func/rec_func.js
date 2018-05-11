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
	var cur_user = sessionStorage.getItem('cur_user');
	console.log(JSON.parse(cur_user));
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