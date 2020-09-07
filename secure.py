#!/usr/bin/python3
# coding: utf-8
from cryptography.fernet import Fernet
import confidential

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


#encrypt("test.sql", confidential.key_encryption)
#decrypt("test", confidential.key_encryption)