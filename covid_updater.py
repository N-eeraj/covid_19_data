import datetime
import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']
date = datetime.date.today().strftime('%d-%b,')
print('Date: '+ date)

def read_data(prompt, file):
	data = []
	print('\n')
	for district in districts :
		count = input(prompt + district + ' :')
		data.append(count)
	data = np.array(data, dtype = int)
	total = data.sum()
	data = np.array(data, dtype = str)
	print('\nTotal:'+ str(total))
	new_line = date + (','.join(data))
	with open(file, 'a') as data_file:
		data_file.write(new_line + '\n')

read_data('Enter the positive cases in ', 'positive.csv')
read_data('Enter the death cases in ', 'death.csv')
