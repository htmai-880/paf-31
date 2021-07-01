import json
from sha2 import sha256
from binascii import unhexlify, hexlify
import hashlib
from struct import pack, unpack, unpack_from
from codecs import encode

def block_hash(block_num):
    with open(str(block_num) + ".json", "r") as f:        
        blocJson_header = json.loads("".join(f.readlines()))['blocks'][0]
        
        ver = pack('<I', blocJson_header['ver']).hex()
        
        prev_nounce = unhexlify(blocJson_header['prev_block'])
        prev_nounce = prev_nounce[::-1].hex()
        
        mrkl_root = unhexlify(blocJson_header['mrkl_root'])
        mrkl_root = mrkl_root[::-1].hex()
        
        time = pack('<I', blocJson_header['time']).hex()
        
        nbits = pack('<I', blocJson_header['bits']).hex()
        
        nonce = pack('<I', blocJson_header['nonce']).hex() 
        
        header_hex = ver + prev_nounce + mrkl_root + time + nbits + nonce
        header_bin = int(header_hex,16)
        diggest = sha256(sha256(header_bin, typ = 'int'), typ = 'int')
        
        return unhexlify(hex(diggest)[2:])[::-1].hex()

if __name__ == "__main__":
    print(block_hash(0))
