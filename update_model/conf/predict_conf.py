LABEL = ['cat', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status', 'prob']
REPEAT_TIME = 10


PARAMS = {
	'min_child_weight' : 10,
	'subsample' : 0.8,
	'colsample_bytree' : 0.8,
	'scale_pos_weight0' : 1.2,
	'silent' : 1,
	'max_depth' : 6,
	'gamma' : 1,
	'nthread' : 6,
	'objective' : "reg:linear",
	'eta' : 0.1,
	# 'base_score' : 1800,
	'eval_metric' : "rmse",
	'seed' : 0,
}

NUM_ROUNDS = 1000

PROB = 3