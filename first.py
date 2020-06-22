import webbrowser

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

elif registered == no:
    print('Redirecting to website')
    webbrowser.open('https://www.google.com')
else:
    print('Your status is: ', no, )
    exit('You are not registered!!! Exiting')

# Output
print('Your registration status is: ' + registered + ' Your name is: ' + name + ' Your age is: ' + age)
print('')
print('Redirecting to website')
webbrowser.open('https://duckduckgo.com')
