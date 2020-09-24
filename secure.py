#!/usr/bin/python3
# coding: utf-8
from cryptography.fernet import Fernet
import confidential


def generate_key():
    """ this function will create one file with one key ,
    you can copy him for paste in your confidential.py file"""
    key = Fernet.generate_key()
    with open("confidential.key", "wb") as key_file:
        key_file.write(key)

def encrypt(filename, key):
    """ AES Encryption : this function uses a key to encrypt files"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypt = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypt)

def decrypt(filename, key):
    """ AES Encryption : this function use a key for decrypt files"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypt_data = f.decrypt(encrypted)
    with open(filename, "wb") as file:
        file.write(decrypt_data)
        
def main():
    generate_key()


if __name__ == "__main__":
    main()
#encrypt("test.sql", confidential.key_encryption)
#decrypt("test", confidential.key_encryption)