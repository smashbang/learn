#  User verification, password confirmation and redirection to login.

import webbrowser

# Users Input Questions
name = input("What is your name? ")
surname = input("What is your surname? ")
registered = input("Have you registered yet? (Yes or No): ")
age = int(input("Whats is your age? "))
password = input("What is the password? ")

# Strings
yes: str = 'Yes'
no: str = 'No'
passwd: str = '12345'
nreg: str = 'Not registered'
reg: str = 'Registered'
check: int = 17

# Evaluation
if password != passwd:
    print("")
    print('Get out of here!!! Come back with the password!!!')
    exit('Password is incorrect!! Exiting')

elif age <= check:
    print("")
    print('You are under aged:',name, surname)
    print('Your registrations status: ' + registered + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:',age)
    print("")
    webbrowser.open('https://www.sesamestreet.org')
    exit('To Young!! \nTo Sesame Street you go!!! \nExiting!!!')

elif registered == yes:
    print("")
    print('Welcome!!!', name, surname)
    print('')
    print('Details: ')

elif registered == no:
    print("")
    print('Your registrations status: ' + nreg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ',age)
    print("")
    print('Redirecting to registration page')
    webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName=GlifWebSignIn&flowEntry=SignUp')
    exit('You are not registered!!! Exiting')

else:
    print('Your status is: ', no,)
    exit('You are not registered!!! Exiting')

# Output
print('Your registration status: ' + reg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ',age)
print('')
print('Redirecting to login website')
webbrowser.open('https://duckduckgo.com')




