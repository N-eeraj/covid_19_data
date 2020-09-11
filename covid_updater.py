import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']

#reading date
day = input('Enter Day : ')
month = input('Enter Month : ')[:3].capitalize()
date = day + '-' + month
print('Date: '+ date)

def fn_save(file, data_list): #function to update a file
	with open(file, 'a') as data_file: #opening file
		data_file.write('\n' + ','.join(data_list)) #updating file

while True:

	pos_list = [date]
	rec_list = [date]
	dead_list = [date]

	for district in districts:
		pos_list.append(input('\nEnter the positive cases in ' + district + ' : ')) #reading positive cases
		rec_list.append(input('Enter the recovered cases in ' + district + ' : ')) #reading recovery cases
		dead_list.append(input('Enter the death cases in ' + district + ' : ')) #reading death cases

	print('\nPositive Cases:', np.array(pos_list[1:], dtype = int).sum())
	print('Recovered Cases:', np.array(rec_list[1:], dtype = int).sum())
	print('Death Cases:', np.array(dead_list[1:], dtype = int).sum())

	if input('\nSave ?').lower() == 'y':
		for files in [('positive.csv', pos_list), ('recovery.csv', rec_list), ('death.csv', dead_list)]:
			fn_save(files[0], files[1]) #updating a file
		print('\nSaved\n')
		break
	else:
		if input('\nTry Again ?').lower() == 'y':
			continue
		else:
			break
