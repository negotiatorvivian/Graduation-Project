function add_to_cart(){
	var point = {
		'latitude' : sessionStorage.getItem('latitude'),
		'longitude' : sessionStorage.getItem('longitude')
	};
	var trade_name = sessionStorage.getItem('trade_name');
	// console.log(trade_name);
	if(point.latitude == null || point.longitude == null)
		return false;
	var list =  sessionStorage.getItem('points');
	var list1 =  sessionStorage.getItem('trade_names');
	if(list1 == null){
		list1 = new Array();
		list1.push(trade_name);
		sessionStorage.setItem('trade_names', JSON.stringify(list1));
	}
	else{
		var name_list = JSON.parse(list1);
		for(var i in name_list){
			if (name_list[i] == trade_name) {
				return false;
			}
		}
		name_list.push(trade_name);
		sessionStorage.setItem('trade_names', JSON.stringify(name_list));
	}

	if(list == null){
		list = new Array();
		list.push(point);
		sessionStorage.setItem('points', JSON.stringify(list));
		
	}
	else{
		var point_list = JSON.parse(list);
		point_list.push(point);
		sessionStorage.setItem('points', JSON.stringify(point_list));
		
	}
}

