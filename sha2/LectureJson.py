import json
from sha2 import sha256
from binascii import unhexlify, hexlify
import hashlib

def lectureJson(bitcoin_num):
    with open(str(bitcoin_num) + ".json", "r") as f:        
        blocJson = json.loads("".join(f.readlines()))
        ver = '0' + str(blocJson['blocks'][0]['ver'])[::-1]
        prev_nounce = blocJson['blocks'][0]['prev_block'][::-1]
        mrkl_root = blocJson['blocks'][0]['mrkl_root'][::-1]
        time = hex(blocJson['blocks'][0]['time'])[2:][::-1]
        nbits = hex(blocJson['blocks'][0]['bits'])[2:][::-1]
        nonce = hex(blocJson['blocks'][0]['nonce'])[2:][::-1]
        header_hex = ver + prev_nounce + mrkl_root + time + nbits + nonce
        header_bin = unhexlify(header_hex)
        #a=int('0x'+bloc, 0)
        return header_bin
    
header = lectureJson(125552)

hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
print(hexlify(hash).decode("utf-8"))
