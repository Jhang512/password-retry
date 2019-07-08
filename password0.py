password = 'a123456'

i = 3

print('You will have 3 chance only...')

while True:
	user_input = input('Please enter password: ')
	if user_input == password:
		print('Login successful!')
		break
	elif user_input != password and i > 1:
		i = i - 1
		print('You still have', i, 'chance')
	else:
		break