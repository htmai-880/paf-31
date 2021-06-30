import json
from sha2 import sha256
from binascii import unhexlify, hexlify
import hashlib
from struct import pack, unpack, unpack_from
from codecs import encode

def block_hash(bitcoin_num):
    with open(str(bitcoin_num) + ".json", "r") as f:        
        blocJson = json.loads("".join(f.readlines()))
        
        ver = pack('<I', blocJson['blocks'][0]['ver']).hex()
        
        prev_nounce = unhexlify(blocJson['blocks'][0]['prev_block'])
        prev_nounce = prev_nounce[::-1].hex()
        
        mrkl_root = unhexlify(blocJson['blocks'][0]['mrkl_root'])
        mrkl_root = mrkl_root[::-1].hex()
        
        time = pack('<I', blocJson['blocks'][0]['time']).hex()
        
        nbits = pack('<I', blocJson['blocks'][0]['bits']).hex()
        
        nonce = pack('<I', blocJson['blocks'][0]['nonce']).hex() 
        
        header_hex = ver + prev_nounce + mrkl_root + time + nbits + nonce
        header_bin = int(header_hex,16)
        diggest = sha256(sha256(header_bin, typ = 'int'), typ = 'int')
        
        return unhexlify(hex(diggest)[2:])[::-1].hex()

if __name__ == "__main__":
    print(block_hash(125552))
