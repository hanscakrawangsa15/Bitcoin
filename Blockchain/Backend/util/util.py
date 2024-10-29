import hashlib
from Crypto.Hash import RIPEMD160
from hashlib import sha256

def hash256(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def hash160(data):
    return RIPEMD160.new(sha256(data).digest()).digest()