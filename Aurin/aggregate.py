import json

agg_state = 'Melbourne (C)'

cities_list = ['Melbourne','Port Phillip','Yarra','Banyule','Darebin','Hume','Valley','Moreland','Boroondara','Knox','Manningham','Maroondah','Whitehorse','Bayside','Casey','Greater Dandenong','Frankston','Glen Eira','Kingston','Monash','Stonnington','Brimbank','Hobsons Bay','Maribyrnong','Melton','Wyndham']

data_year = ['melb2012','melb2013','melb2014','melb2015','melb2016']


def do_magic(content):
	grid = {}
	grid['lga_name11'] = agg_state
	grid['a_total'] = 0
	grid['b_total'] = 0
	grid['c_total'] = 0
	grid['d_total'] = 0
	grid['e_total'] = 0
	grid['f_total'] = 0
	grid['estimated_population'] = 0 
	grid['ref_period'] = '' 
	for cities in content['features']:
		for my_city in cities_list:
			if my_city + ' (C)' == cities['properties']['lga_name11']:
				grid['a_total'] += cities['properties']['a_total']
				grid['b_total'] += cities['properties']['b_total']
				grid['c_total'] += cities['properties']['c_total']
				grid['d_total'] += cities['properties']['d_total']
				grid['e_total'] += cities['properties']['e_total']
				grid['f_total'] += cities['properties']['f_total']
				grid['ref_period'] = cities['properties']['ref_period']
				grid['estimated_population'] += cities['properties']['lga_erp']
	print (grid)
				

for file in data_year:
	file_name = file + '.json'
	with open(file_name) as fs:
		content = json.load(fs)
		do_magic(content)
