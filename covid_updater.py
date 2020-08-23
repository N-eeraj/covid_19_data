import datetime
import numpy as np

districts = ['Kasaragod', 'Kannur', 'Wayanad', 'Kozhikode', 'Malappuram', 'Palakkad', 'Thrissur', 'Ernakulam', 'Idukki',
		'Kottayam', 'Pathanamthitta', 'Alapuzha', 'Kollam', 'Thiruvananthapuram']
date = datetime.date.today().strftime('\n%d-%b,')
data = []
print('Date:'+ date)

for district in districts :
	count = input('Enter the positive cases in ' + district + ' :')
	data.append(count)

data = np.array(data, dtype = int)
total = data.sum()
data = np.array(data, dtype = str)
print('\nTotal:'+ str(total))

new_line = date + (','.join(data))

with open('positive.csv','a') as pos_data_file:
	pos_data_file.write(new_line)
