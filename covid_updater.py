import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']

#reading date
day = input('Enter Day : ')
month = input('Enter Month : ')[:3].capitalize()
date = month + '-' + day
print('Date: '+ date)

def read_data(prompt, file):
	data = []
	print('\n')
	for district in districts :
		count = input(prompt + district + ' :')
		data.append(count) #making a list of new entries
	data = np.array(data, dtype = int) #converting list to numpy array
	total = data.sum() #totalling the count
	data = np.array(data, dtype = str)
	print('\nTotal:'+ str(total))
	new_line = date + (','.join(data)) #transforming array to a comma sepsrated line as new line
	with open(file, 'a') as data_file:
		data_file.write('\n' + new_line) #appending the new line to the file

#adding data to the respective files
read_data('Enter the positive cases in ', 'positive.csv')
read_data('Enter the death cases in ', 'death.csv')
read_data('Enter the recovery cases in ', 'recovery.csv')
