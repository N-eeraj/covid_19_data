import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from termcolor import colored

#dataframe creation from csv files
pos_df = pd.read_csv('positive.csv')
death_df = pd.read_csv('death.csv')
recover_df = pd.read_csv('recovery.csv')

## Work Here - Error : Addition Error 'Date'
#active_df = pos_df[1:] - (recover_df[1:] + death_df[1:]) #calculating active cases
#print(active_df)
#exit()

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
		district_result = True
	else:
		district_result = False
	return district_result

while True:
	try:
		case_type = read_msg('\n1.Positive Cases\n2.Death Tolls\n3.Recoved Cases\nPress "X" to exit\n\n')
	except KeyboardInterrupt:
		fn_exit() #exit on Ctrl+C

	if case_type in ['1', 'positive', 'pos']:
		print('Accessing COVID Positive Data\n')
		df = pos_df[pos_df.columns[1:]] #excluding date column from the dataframe
		df.index = np.array(pos_df['Date']) #setting date column as index
		plot_title = 'COVID Positive Cases '
		clr_code = '#03F'

	elif case_type in ['2', 'death', 'dead']:
		print('Accessing COVID Death Data\n')
		df = death_df[death_df.columns[1:]] #excluding date column from the dataframe
		df.index = np.array(death_df['Date']) #setting date column as index
		plot_title = 'COVID Death Reports '
		clr_code = '#A00'

	elif case_type in ['3', 'recovery', 'recovered']:
		print('Accessing COVID Recovery Data\n')
		df = recover_df[pos_df.columns[1:]] #excluding date column from the dataframe
		df.index = np.array(recover_df['Date']) #setting date column as index
		plot_title = 'COVID Recovered Cases '
		clr_code = '#070'

	elif case_type in ['x', 'exit', 'quit']:
		fn_exit()
	else:
		print_error('Invalid Input\n')
		continue

	#confirming date in dataframe
	def read_date():
		search_month = input('\nEnter Month: ').capitalize()[:3]
		search_day = input('Enter Date: ')
		search_date = search_day + '-' + search_month
		if search_date not in df.index:
			print_error('Date not found\n')
			return True
		else:
			return search_date

	try:
		search_type = read_msg('\n1.Date vs Case\n2.Date Results\n3.Date & Case Based Search\nPress "Z" to go back\nPress "X" to exit\n\n')
	except KeyboardInterrupt:
		fn_exit() #exit on Ctrl+C

	if search_type in ['1', 'datevscase', 'plot', 'vs']:
		plot_title  += 'in '
		district = read_district()
		try:
			plt.plot(df[district], clr_code)
			plt.title(plot_title + district)
		except KeyError:
			if district == False:
				print_error('District Not Found')
				continue
			plt.plot(df[df.columns].sum(axis = 1), clr_code) #totaling the district counts
			plt.title(plot_title + 'Kerala')
		plt.xlabel('No.of Days')
		plt.ylabel('Cases Reported')
		plt.show()

	elif search_type in ['2', 'date', 'results']:
		date = read_date()
		if date != True:
			plt.bar(list(districts[district][-1].upper() for district in districts), df.loc[date], color = clr_code)
			plt.xticks(rotation = 15)
			plt.show()
		## Work Here

	elif search_type in ['3', 'search', 'date&case', 'date and case']:
		district = read_district()
		date = read_date()
		try:
			if date != True:
				print(df[district][date])
		except KeyError:
			if district == False:
				print_error('District Not Found')
				continue
			print(df[df.columns].sum(axis = 1)[date]) #totaling the district counts & finding date

	elif search_type in ['z', 'back', 'go back', 'goback']:
		continue
	elif search_type in ['x', 'exit', 'quit']:
		fn_exit()
	else:
		print_error('Invalid Input\n')
		continue
