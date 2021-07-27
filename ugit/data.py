import os
import hashlib

GET_DIR = '.ugit'

def init():
    os.makedirs(GET_DIR)
    os.makedirs(f'{GET_DIR}/objects')

def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    # in layman's terms: use data to create a hash which becomes the folder name
    oid = hashlib.sha1(data).hexdigest()
    # 'wb' = open in binary mode.
    # note that the file is oid.
    with open(f'{GET_DIR}/objects/{oid}', 'wb') as out:
        out.write(obj)
    return oid

def get_object(oid, expected='blob'):
    with open(f'{GET_DIR}/objects/{oid}', 'rb') as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f'Expected{expected}, got{type_}'
    return content
