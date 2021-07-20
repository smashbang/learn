#  User verification, password confirmation and redirection to login.

import webbrowser

# Users Input Questions
name = input("What is your name? ")
surname = input("What is your surname? ")
age = input("Whats is your age? ")
registered = input("Have you registered yet? (Yes or No): ")
password = input("What is the password? ")

# Strings
yes: str = 'Yes'
no: str = 'No'
passwd: str = '12345'
nreg: str = 'Not registered'
reg: str = 'Registered'

# Evaluation
if password != passwd:
    print("")
    print('Get out of here!!! Come back with the password!!!')
    exit('Password is incorrect!! Exiting')

elif registered == yes:
    print("")
    print('Welcome!!!', name, surname)
    print('')
    print('Details: ')

elif registered == no:
    print("")
    print('Your registrations status: ' + nreg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ' + age)
    print("")
    print('Redirecting to Google')
    webbrowser.open('https://www.google.com')
    exit('You are not registered!!! Exiting')

else:
    print('Your status is: ', no, )
    exit('You are not registered!!! Exiting')

# Output
print('Your registration status: ' + reg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ' + age)
print('')
print('Redirecting to login website')
webbrowser.open('https://duckduckgo.com')
