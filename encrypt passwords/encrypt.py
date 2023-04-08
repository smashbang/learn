from cryptography.fernet import Fernet

# generate a secret key
key = Fernet.generate_key()

# save the key to a file for future use
with open( 'key.key', 'wb' ) as key_file:
    key_file.write(key)

# load the key from the file
with open( 'key.key', 'rb' ) as key_file:
    key = key_file.read()

# read the contents of the config file
with open( 'config.ini', 'rb' ) as config_file:
    config = config_file.read()

# create a Fernet object with the key
fernet = Fernet(key)

# encrypt the config file contents
encrypted = fernet.encrypt(config)

# write the encrypted data to a new file
with open( '../config.ini.encrypted', 'wb' ) as encrypted_file:
    encrypted_file.write(encrypted)


