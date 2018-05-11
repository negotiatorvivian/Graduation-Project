BLACK_FRI_MODEL = 'blackFri_1'
# BLACK_FRI_MODEL = 'blackFri_2'


PARAMS = {
	'min_child_weight' : 10,
	'subsample' : 0.7,
	'colsample_bytree' : 0.7,
	'scale_pos_weight0' : .8,
	'silent' : 1,
	'max_depth' : 6,
	'nthread' : 6,
	'objective' : "reg:linear",
	'eta' : 0.1,
	'base_score' : 1800,
	'eval_metric' : "rmse",
	'seed' : 0,
}


LABEL = ['cat', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']


BEST_NTREE_LIMIT = 975
# LABEL_ALL = ['User_ID', 'cat', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status', 'Purchase', 'aver', 'prob']

# RESULT_LABEL = ["Purchase","aver","prob"]


MISSING_VALUE = -999.0


LINES = 100

CATEGORY_NUM = 20