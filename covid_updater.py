import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']

#reading date
day = input('Enter Day : ')
month = input('Enter Month : ')[:3].capitalize()
date = day + '-' + month
print('Date: '+ date)

pos_list = [date]
rec_list = [date]
dead_list = [date]

def fn_save(file, data_list): #function to update a file
	with open(file, 'a') as data_file: #opening file
		data_file.write('\n' + ','.join(data_list)) #updating file

for district in districts:
	pos_list.append(input('\nEnter the positive cases in ' + district + ' : ')) #reading positive cases
	rec_list.append(input('Enter the recovered cases in ' + district + ' : ')) #reading recovery cases
	dead_list.append(input('Enter the death cases in ' + district + ' : ')) #reading death cases

for files in [('positive.csv', pos_list), ('recovery.csv', rec_list), ('death.csv', dead_list)]:
	print('\n' + files[0][:-4].capitalize(), 'Cases:' , np.array(files[1][1:], dtype = int).sum()) #calculate sums
	fn_save(files[0], files[1]) #updating a file
