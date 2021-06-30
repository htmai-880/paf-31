import json
from Sha256 import sha256
from binascii import unhexlify, hexlify
import hashlib
import requests
from struct import pack, unpack, unpack_from
from codecs import encode

def block_hash(num):
    #with open("BlocBitcoin.json", "r") as f:
    url = "https://blockchain.info/block-height/{}?format=json".format(num)
    donneestexte = requests.get(url)      
    blocJson = json.loads(donneestexte.content)['blocks'][0]
    
    ver = pack('<I', blocJson['ver']).hex()
    
    prev_nounce = unhexlify(blocJson['prev_block'])
    prev_nounce = prev_nounce[::-1].hex()
    
    mrkl_root = unhexlify(blocJson['mrkl_root'])
    mrkl_root = mrkl_root[::-1].hex()
    
    time = pack('<I', blocJson['time']).hex()
    
    nbits = pack('<I', blocJson['bits']).hex()
    
    nonce = pack('<I', blocJson['nonce']).hex() 
    
    header_hex = ver + prev_nounce + mrkl_root + time + nbits + nonce
    header_bin = int(header_hex,16)
    diggest = sha256(sha256(header_bin, typ = 'int'), typ = 'int')
    
    return unhexlify(hex(diggest)[2:])[::-1].hex()

if __name__ == "__main__":
    print(block_hash(0))
