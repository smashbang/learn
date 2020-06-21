# User Input Questions
name = input("What is your name? ")
age = input("Whats is your age? ")
registered = input("Have you registered yet? (Yes or No): ")

# Strings
yes: str = 'Yes'
yes1: str = 'yes'
no: str = 'No'

# Evaluation
if registered == yes.lower() == yes1:
    print('Your status is: ', yes)
    print('Welcome!!!', name)
    print('')
    print('Details: ')
else:
    print('Your status is: ', no, )
    exit('You are not registered!!! Exiting')

# Output
print('Your name is:', name)
print('Your age is:', age)
print('Registration Status: ', registered)
