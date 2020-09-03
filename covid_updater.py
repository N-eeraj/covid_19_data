import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']

#reading date
day = input('Enter Day : ')
month = input('Enter Month : ')[:3].capitalize()
date = day + '-' + month
print('Date: '+ date)

pos_list = [date]
recovery_list = [date]
death_list = [date]

def fn_save(file, data_list):
	with open(file, 'a') as data_file:
		data_file.write('\n' + ','.join(data_list))

for district in districts:
	pos_list.append(input('\nEnter the positive cases in ' + district + ' : '))
	recovery_list.append(input('Enter the recovered cases in ' + district + ' : '))
	death_list.append(input('Enter the death cases in ' + district + ' : '))

for files in [('positive.csv', pos_list), ('recovery.csv', recovery_list), ('death.csv', death_list)]:
	print('\n' + files[0][:-4].capitalize(), 'Cases:' , np.array(files[1][1:], dtype = int).sum())
	fn_save(files[0], files[1])

#def read_data(prompt, file):
#	data = []
#	print('\n')
#	for district in districts :
#		count = input(prompt + district + ' :')
#		data.append(count) #making a list of new entries
#	data = np.array(data, dtype = int) #converting list to numpy array
#	total = data.sum() #totalling the count
#	data = np.array(data, dtype = str)
#	print('\nTotal:'+ str(total))
#	new_line = date + ',' + (','.join(data)) #transforming array to a comma sepsrated line as new line
#	with open(file, 'a') as data_file:
#		data_file.write('\n' + new_line) #appending the new line to the file

#adding data to the respective files
#read_data('Enter the positive cases in ', 'positive.csv')
#read_data('Enter the death cases in ', 'death.csv')
#read_data('Enter the recovery cases in ', 'recovery.csv')
