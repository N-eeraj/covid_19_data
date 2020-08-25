import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('positive.csv', 'r') as pos_data_file:
	pos_data_lines = pos_data_file.readlines()

#dictionary to turn it into a dataframe
pos_data_dict = {'kasaragod': np.array([]), 'kannur': np.array([]), 'wayanad': np.array([]), 'kozhikode': np.array([]),
	'malappuram': np.array([]), 'palakkad': np.array([]), 'thrissur': np.array([]), 'ernakulam': np.array([]),
	'idukki': np.array([]), 'kottayam': np.array([]), 'pathanamthitta': np.array([]), 'alappuzha': np.array([]),
	'kollam': np.array([]), 'thiruvananthapuram': np.array([])}
#date list to store dates to use as indices
date = np.array([])
#district_codes
tvm = ['1', 'thiruvananthapuram', 'tvm']
klm = ['2', 'kollam', 'klm']
alp = ['3', 'alappuzha', 'alp']
pta = ['4', 'pathanamthitta', 'pta']
ktm = ['5', 'kottayam', 'ktm']
idk = ['6', 'idukki', 'idk']
ekm = ['7', 'ernakulam', 'ekm']
tsr = ['8', 'thrissur', 'tsr']
pkd = ['9', 'palakkad', 'pkd']
mpm = ['10', 'malappuram', 'mpm']
kkd = ['11', 'kozhikode', 'kkd']
wyd = ['12', 'wayanad', 'wyd']
knr = ['13', 'kannur', 'knr']
kgd = ['14', 'kasaragod', 'kgd']
total = ['0', 'kerala', 'kl', 'all', 'total']

#read  pos_data to pos_dictionary
for pos_data_line in pos_data_lines[1:]:
	pos_data_cell = pos_data_line.split(',')
	date = np.append(date, pos_data_cell[0])
	pos_data_dict['kasaragod'] = np.append(pos_data_dict['kasaragod'], pos_data_cell[1]).astype(np.int)
	pos_data_dict['kannur'] = np.append(pos_data_dict['kannur'], pos_data_cell[2]).astype(np.int)
	pos_data_dict['wayanad'] = np.append(pos_data_dict['wayanad'], pos_data_cell[3]).astype(np.int)
	pos_data_dict['kozhikode'] = np.append(pos_data_dict['kozhikode'], pos_data_cell[4]).astype(np.int)
	pos_data_dict['malappuram'] = np.append(pos_data_dict['malappuram'], pos_data_cell[5]).astype(np.int)
	pos_data_dict['palakkad'] = np.append(pos_data_dict['palakkad'], pos_data_cell[6]).astype(np.int)
	pos_data_dict['thrissur'] = np.append(pos_data_dict['thrissur'], pos_data_cell[7]).astype(np.int)
	pos_data_dict['ernakulam'] = np.append(pos_data_dict['ernakulam'], pos_data_cell[8]).astype(np.int)
	pos_data_dict['idukki'] = np.append(pos_data_dict['idukki'], pos_data_cell[9]).astype(np.int)
	pos_data_dict['kottayam'] = np.append(pos_data_dict['kottayam'], pos_data_cell[10]).astype(np.int)
	pos_data_dict['pathanamthitta'] = np.append(pos_data_dict['pathanamthitta'], pos_data_cell[11]).astype(np.int)
	pos_data_dict['alappuzha'] = np.append(pos_data_dict['alappuzha'], pos_data_cell[12]).astype(np.int)
	pos_data_dict['kollam'] = np.append(pos_data_dict['kollam'], pos_data_cell[13]).astype(np.int)
	pos_data_dict['thiruvananthapuram'] = np.append(pos_data_dict['thiruvananthapuram'], pos_data_cell[14].strip()).astype(np.int)

#totalling positive cases
first = True
for district in pos_data_dict.keys():
	if first:
		pos_total = (pos_data_dict[district])
		first = False
	else:
		pos_total += (pos_data_dict[district])
pos_total.astype(np.int)

#data_frame for positive cases
pos_df = pd.DataFrame(pos_data_dict)
pos_df.index = date
#print(pos_df)

def read_date():
	search_month = input('\nEnter Short Month: ').capitalize()[:3]
	search_day = input('Enter Date: ')
	search_date = search_day + '-' + search_month
	if search_date not in pos_df.index:
		print('Error Date not found\n')
		return True
	else:
		return search_date

while True:
	plot_selection = input('1. Date vs Cases\n2. Cases on a specific date\n3. Cases on specific date & district\n')
	if plot_selection == '1':
		plot_option = input('\nTotal\n1.Thiruvananthapuram\n2.Kollam\n3.Pathanamthitta\n4.Alappuzha\n5.Kottayam\n6.Idukki\n7.Ernakulam' +
					'\n8.Thrissur\n9.Palakkad\n10.Malappuram\n11.Kozhikode\n12.Wayanad\n13.Kannur\n14.Kasaragod\n\n').lower()
		plot_title = 'Positive COVID 19 Cases'
		if plot_option in total:
			print('Kerala')
			plt.plot(date, pos_total)
			max_y = pos_total.max()
		elif plot_option in tvm:
			print('Thiruvananthapuram')
			plt.plot(pos_df['thiruvananthapuram'])
			max_y = pos_df['thiruvananthapuram'].max()
			plot_title += ' in Thiruvananthapuram'
		elif plot_option in klm:
			print('Kollam')
			plt.plot(pos_df['kollam'])
			max_y = pos_df['kollam'].max()
			plot_title += ' in Kollam'
		elif plot_option in pta:
			print('Pathanamthitta')
			plt.plot(pos_df['pathanamthitta'])
			max_y = pos_df['pathanamthitta'].max()
			plot_title += ' in Pathhanamthitta'
		elif plot_option in alp:
			print('Alappuzha')
			plt.plot(pos_df['alappuzha'])
			max_y = pos_df['alappuzha'].max()
			plot_title += ' in Alappuzha'
		elif plot_option in ktm:
			print('Kottayam')
			plt.plot(pos_df['kottayam'])
			max_y = pos_df['kottayam'].max()
			plot_title += ' in Kottayam'
		elif plot_option in idk:
			print('Idukki')
			plt.plot(pos_df['idukki'])
			max_y = pos_df['idukki'].max()
			plot_title += ' in Idukki'
		elif plot_option in ekm:
			print('Ernakulam')
			plt.plot(pos_df['ernakulam'])
			max_y = pos_df['ernakulam'].max()
			plot_title += ' in Ernakulam'
		elif plot_option in tsr:
			print('Thrissur')
			plt.plot(pos_df['thrissur'])
			max_y = pos_df['thrissur'].max()
			plot_title += ' in Thrissur'
		elif plot_option in pkd:
			print('Palakkad')
			plt.plot(pos_df['palakkad'])
			max_y = pos_df['palakkad'].max()
			plot_title += ' in Palakkad'
		elif plot_option in mpm:
			print('Malappuram')
			plt.plot(pos_df['malappuram'])
			max_y = pos_df['malappuram'].max()
			plot_title += ' in Malappuram'
		elif plot_option in kkd:
			print('Kozhikode')
			plt.plot(pos_df['kozhikode'])
			max_y = pos_df['kozhikode'].max()
			plot_title += ' in Kozhikode'
		elif plot_option in wyd:
			print('Wayanad')
			plt.plot(pos_df['wayanad'])
			max_y = pos_df['wayanad'].max()
			plot_title += ' in Wayanad'
		elif plot_option in knr:
			print('Kannur')
			plt.plot(pos_df['kannur'])
			max_y = pos_df['kannur'].max()
			plot_title += ' in Kannur'
		elif plot_option in kgd:
			print('Kasaragod')
			plt.plot(pos_df['kasaragod'])
			max_y = pos_df['kasaragod'].max()
			plot_title += ' in Kasaragod'
		else:
			print('Exiting...')
			exit()

		yhigh = int(max_y * 1.1)
		plt.title(plot_title)
		plt.xlabel('Days')
		plt.ylabel('Cases Reported')
		plt.ylim(0, yhigh)
		plt.show()

#	elif plot_selection == '2' :
#	

	elif plot_selection == '3' :
		date_input = read_date()
		if date_input == True:
			continue
		search_district = input('Enter District: ').lower()
		try:
			search_result = pos_df[search_district][date_input]
		except KeyError:
			print('\nError District not found\n')
			continue
		print('Cases on ' + date_input + ' in ' + search_district + '\n')
		print(search_result)
	else:
		print('Exiting...')
		exit()
