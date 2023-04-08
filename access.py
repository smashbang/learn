#  User verification, with password confirmation and redirection to login.

import configparser
import webbrowser

from cryptography.fernet import Fernet

# Load the encryption key from file
with open('key.key', 'rb') as file:
    key = file.read()

# Create a Fernet cipher
cipher = Fernet(key)

# Read the contents of the config.ini file
with open('config.ini.encrypted', 'rb') as file:
    data = file.read()

# Decrypt thr data using the cipher
decrypted_data = cipher.decrypt(data)

# Parse the decrypted data as a config file
config = configparser.ConfigParser()
config.read_string(decrypted_data.decode('utf-8'))

# Get the password from the config file
passwd = config.get('User', 'password')

# User verification, password confirmation and redirection to login.
name = input("What is your name? ")
surname = input("What is your surname? ")
registered = input("Have you registered yet? (yes or no): ")
age = int(input("What is your age? "))
password = input("What is the password? ")

# Strings
yes = 'yes'.upper().lower()
no = 'no'.upper().lower()
noreg = 'Not registered'.upper().lower()
reg = 'Registered'.upper().lower()
check = 16

# Evaluation
if password != passwd:
    print("")
    print('Get out of here!!!' '\nCome back with the password!!!' '\n')
    exit('Password is incorrect!!' '\n')

elif age <= check:
    print("")
    print('You are underage:', name, surname)
    print('Your registration status: ' + registered + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:', age)
    print("")
    webbrowser.open('https://www.sesamestreet.org')
    exit('Too young!! ' '\nTo Sesame Street you go!!!' '\n')

elif registered == yes:
    print("")
    print('Welcome!!!', name, surname)
    print('')
    print('Details: ')

elif registered == no:
    print("")
    print('Your registration status: ' + noreg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ', age)
    print("")
    print('Redirecting to registration page''\n')
    webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google'
                    '.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName'
                    '=GlifWebSignIn&flowEntry=SignUp')
    exit('You are not registered!!!' '\nExiting!!!')
else:
    print('Your status is:', no,)
    exit('\nYou are not registered!!!' '\n Exiting!!!' '\n')

# Output
print('Your registration status: ' + reg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is: ', age)
print('')
print('Redirecting to login website' '\n')
webbrowser.open('https://duckduckgo.com')

