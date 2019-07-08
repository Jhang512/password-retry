password = 'a123456'

print('You will have 3 chance only...')

i = 3

while i != 0:
	user_input = input('Please enter your password:..')
	if user_input == password:
		print('Login successful!')
		break
	else:
		i = i - 1
		print('Wrong Password!, You still have', i, 'chance')
		
print('Aborted.')