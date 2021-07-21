import os
import hashlib

GET_DIR = '.ugit'

def init():
    os.makedirs(GET_DIR)
    os.makedirs(f'{GET_DIR}/objects')

def hash_object(data):
    # in layman's terms: use data to create a hash which becomes the folder name
    oid = hashlib.sha1(data).hexdigest()
    # 'wb' = open in binary mode
    with open(f'{GET_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid

def get_object(oid):
     with open(f'{GET_DIR}/objects/{oid}', 'rb') as f:
         return f.read()
