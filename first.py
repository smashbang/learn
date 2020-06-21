# User Input Questions
name = input("What is your name? ")
age = input("Whats is your age? ")
registered = input("Have you registered yet? (Yes or No): ")

# Strings
yes: str = 'Yes'
no: str = 'No'

# Evaluation
if registered == yes:
    print("")
    print('Welcome!!!', name)
    print('')
    print('Details: ')
else:
    print('Your status is: ', no, )
    exit('You are not registered!!! Exiting')

# Output
print('Your registration status is: ', registered)
print('Your name is:', name)
print('Your age is:', age)

