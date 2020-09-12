import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from termcolor import colored

### reading csv files into dataframes
pos_df = pd.read_csv('positive.csv', index_col = 0)
dth_df = pd.read_csv('death.csv', index_col = 0)
rec_df = pd.read_csv('recovery.csv', index_col = 0)

### computing total cases of each day
pos_df['Total'] = pos_df.sum(axis = 1)
dth_df['Total'] = dth_df.sum(axis = 1)
rec_df['Total'] = rec_df.sum(axis = 1)

#computing active cases
act_df = pos_df - (rec_df + dth_df)
for row in range(1, len(act_df)): #cumilating active cases
	act_df.iloc[row]  += act_df.iloc[row - 1]

#district selectors
districts = {
		'kgd' : ['14', 'kasaragod', 'kgd'], 'knr' : ['13', 'kannur', 'knr'], 'wyd' : ['12', 'wayanad', 'wyd'],
		'kkd' : ['11', 'kozhikode', 'kkd'], 'mpm' : ['10', 'malappuram', 'mpm'], 'pkd' : ['9', 'palakkad', 'pkd'],
		'tsr' : ['8', 'thrissur', 'tsr'], 'ekm' : ['7', 'ernakulam', 'ekm'], 'idk' : ['6', 'idukki', 'idk'],
		'ktm' : ['5', 'kottayam', 'ktm'], 'pta' : ['4', 'pathanamthitta', 'pta'], 'alp' : ['3', 'alappuzha', 'alp'],
		'klm' : ['2', 'kollam', 'klm'], 'tvm' : ['1', 'thiruvananthapuram', 'tvm']
		}

#function to make imput prompt white
def read_msg(prompt):
	input_read = input(colored(prompt, 'white')).lower()
	return input_read
#funtion to make error msg red
def print_error(error_msg):
	print(colored('Error! ' + error_msg, 'red'))

#exit function with a msg
def fn_exit():
	print('\nExiting...\n')
	exit()

#reading districts
def read_district():
	search_district = read_msg('0.All Kerala\n1.Thiruvananthapuram\n2.Kollam\n3.Pathanamthitta\n4.Alappuzha\n5.Kottayam\n6.Idukki\n7.Ernakulam' +
				'\n8.Thrissur\n9.Palakkad\n10.Malappuram\n11.Kozhikode\n12.Wayanad\n13.Kannur\n14.Kasaragod\n\n').lower()
	if search_district in districts['tvm']:
		district_result = 'Thiruvananthapuram'
	elif search_district in districts['klm']:
		district_result = 'Kollam'
	elif search_district in districts['alp']:
		district_result = 'Alappuzha'
	elif search_district in districts['pta']:
		district_result = 'Pathanamthitta'
	elif search_district in districts['ktm']:
		district_result = 'Kottayam'
	elif search_district in districts['idk']:
		district_result = 'Idukki'
	elif search_district in districts['ekm']:
		district_result = 'Ernakulam'
	elif search_district in districts['tsr']:
		district_result = 'Thrissur'
	elif search_district in districts['pkd']:
		district_result = 'Palakkad'
	elif search_district in districts['mpm']:
		district_result = 'Malappuram'
	elif search_district in districts['kkd']:
		district_result = 'Kozhikode'
	elif search_district in districts['wyd']:
		district_result = 'Wayanad'
	elif search_district in districts['knr']:
		district_result = 'Kannur'
	elif search_district in districts['kgd']:
		district_result = 'Kasaragod'
	elif search_district in ['0', 'kl', 'kerala', 'all']:
		district_result = 'Total'
	else:
		district_result = False
	return district_result

while True:
	### reading what dataframe to access
	try:
		case_type = read_msg('\n1.Positive Cases\n2.Death Tolls\n3.Recoved Cases\n4.Active Cases\nPress "X" to exit\n\n')
	except KeyboardInterrupt:
		fn_exit() #exit on Ctrl+C

	if case_type in ['1', 'positive', 'pos']:
		print('Accessing COVID Positive Data\n')
		df = pos_df
		plot_title = 'COVID Positive Cases '
		clr_code = '#03F'

	elif case_type in ['2', 'death', 'dead']:
		print('Accessing COVID Death Data\n')
		df = dth_df
		plot_title = 'COVID Death Reports '
		clr_code = '#A00'

	elif case_type in ['3', 'recovery', 'recovered']:
		print('Accessing COVID Recovery Data\n')
		df = rec_df
		plot_title = 'COVID Recovered Cases '
		clr_code = '#070'

	elif case_type in ['4', 'active', 'ongoing']:
		print('Accessing Active COVID Data\n')
		df = act_df
		plot_title = 'COVID Active Cases '
		clr_code = '#AA0'

	elif case_type in ['x', 'exit', 'quit']:
		fn_exit()
	else:
		print_error('Invalid Input\n')
		continue

	#confirming date in dataframe
	def read_date():
		search_month = read_msg('\nEnter Month: ').capitalize()[:3]
		search_day = read_msg('Enter Date: ')
		search_date = search_day + '-' + search_month
		if search_date not in df.index:
			print_error('Date not found\n')
			return False
		else:
			return search_date

	# reading how to show data
	try:
		search_type = read_msg('\n1.Date vs Case\n2.Date Results\n3.Date & Case Based Search\nPress "Z" to go back\nPress "X" to exit\n\n')
	except KeyboardInterrupt:
		fn_exit() #exit on Ctrl+C

	if search_type in ['1', 'datevscase', 'plot', 'vs']: #date vs case graph
		plot_title  += 'in '
		district = read_district()
		try:
			plt.plot(df[district], clr_code)
			plt.title(plot_title + district)
		except KeyError:
			if district == False:
				print_error('District Not Found')
				continue
			plt.plot(df[district], clr_code)
			plt.title(plot_title + 'Kerala')
		plt.xlabel('No. of Days')
		plt.ylabel('Cases Reported')
		plt.show()

	elif search_type in ['2', 'date', 'results']: #cases on a date bar graph
		date = read_date()
		if date != False:
			plt.bar(list(districts[district][-1].upper() for district in districts), df.loc[date][:-1], color = clr_code)
			plt.xticks(rotation = 15)
			plt.title(plot_title + ' on ' + date)
			plt.xlabel('Districts')
			plt.ylabel('Cases Reported')
			plt.show()

	elif search_type in ['3', 'search', 'date&case', 'date and case']: #return data of cases on a date
		district = read_district()
		date = read_date()
		try:
			if date != True:
				print(df[district][date])
		except KeyError:
			if district == False:
				print_error('District Not Found')
				continue
			print(df.loc[date])

	elif search_type in ['z', 'back', 'go back', 'goback']:
		continue
	elif search_type in ['x', 'exit', 'quit']:
		fn_exit()
	else:
		print_error('Invalid Input\n')
		continue
