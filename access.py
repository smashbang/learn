#  User verification, with password confirmation and redirection to login.

import configparser
import secrets
import webbrowser

from cryptography.fernet import Fernet

# Load the encryption key from file
with open( 'key/key.key', 'rb' ) as file:
    key = file.read()

# Create a Fernet cipher
cipher = Fernet(key)

# Read the contents of the config.ini file
with open('config.ini.encrypted', 'rb') as file:
    data = file.read()

# Decrypt the data using the cipher
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
check = 17

# Evaluation
if not secrets.compare_digest(password, passwd):
    print("")
    print('Get out of here!!!' '\nCome back with the password!!!' '\n')
    print('Password is incorrect!!' '\n')
    exit()

elif age <= check:
    print("")
    print('You are underage:', name, surname)
    print('Your registration status: ' + registered + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:', age, 'you do not qualify!!!')
    print("")
    webbrowser.open('https://www.sesamestreet.org')
    print('Too young!! ' '\nTo Sesame Street you go!!!' '\n')
    exit()

elif registered == yes:
    print("")
    print('Welcome!!!', name, surname)
    print('')
    print('Details: ')

elif registered == no:
    print("")
    print('Your registration status: ' + noreg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:', age, 'you qualify!!!')
    print("")
    print ('You are not registered!!!' '\n')
    print('Redirecting to registration page''\n')
    webbrowser.open('https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fmyaccount.google'
                    '.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dcreate-account-button&flowName'
                    '=GlifWebSignIn&flowEntry=SignUp')
    exit()

# Output
print('Your registration status: ' + reg + '\nYour name is: ' + name + ' ' + surname + '\nYour age is:', age, 'you qualify!!!')
print('')
print('Redirecting to login website' '\n')
webbrowser.open('https://accounts.google.com/v3/signin/identifier?dsh=S2013952555%3A1680986621172191&continue=https'
                '%3A%2F%2Fwww.google.com.au%2F%3Fclient%3Dsafari&ec=GAZAmgQ&hl=en&ifkv=AQMjQ7Saq-u7KlqUTVLkqm'
                'AuGEpX9aeekSqWjkbV1OYnDEMf6tF19ky1gM-4BP2d-J17-i8Zpzib&passive=true&flowName=GlifWebSignIn&f'
                'lowEntry=ServiceLogin')

