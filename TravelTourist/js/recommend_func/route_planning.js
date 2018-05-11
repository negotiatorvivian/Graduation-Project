function add_to_cart(){
	var point = {
		'latitude' : sessionStorage.getItem('latitude'),
		'longitude' : sessionStorage.getItem('longitude')
	};
	if(point.latitude == null || point.longitude == null)
		return false;
	var list =  sessionStorage.getItem('points');
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
	console.log(sessionStorage.getItem('points'));

}