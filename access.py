#  User verification, with randomly generated password confirmation and redirection to login.

import secrets
import string
import webbrowser

alphabet = string.ascii_letters + string.digits

# Users Input Questions
name = input("What is your name? ")
surname = input("What is your surname? ")
registered = input("Have you registered yet? (Yes or No): ")
age = int(input("Whats is your age? "))
password = input("What is the password? ")

# Strings
yes: str = 'Yes'.upper().lower()
no: str = 'No'.upper().lower()
notreg: str = 'Not registered'.upper().lower()
reg: str = 'Registered'.upper().lower()
check: int = 17

while True:
    passwd = ''.join(secrets.choice(alphabet) for i in range(5))
    if (any(c.islower() for c in passwd)
            and any(c.isupper() for c in passwd)
            and sum(c.isdigit() for c in passwd) >= 3):
        break

# Evaluation
if password != passwd:
    print("")
    print('Get out of here!!! Come back with the password!!!')
    exit('\nPassword is incorrect!! \nExiting!!!')

elif age <= check:
    print("")
    print('You are under aged:', name, surname)
    print('Your registration status: ' + registered + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:', age)
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
    print('Your registration status: ' + notreg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ', age)
    print("")
    print('Redirecting to registration page')
    webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google'
                    '.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName'
                    '=GlifWebSignIn&flowEntry=SignUp')
    exit('\nYou are not registered!!! \nExiting!!!')

else:
    print('Your status is: ', no,)
    exit('\nYou are not registered!!! \nExiting!!!')

# Output
print('Your registration status: ' + reg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ', age)
print('')
print('Redirecting to login website')
webbrowser.open('https://duckduckgo.com')
