import json
from sha2 import sha256
from binascii import unhexlify, hexlify
import hashlib
from struct import pack, unpack, unpack_from

def lectureJson(bitcoin_num):
    with open(str(bitcoin_num) + ".json", "r") as f:        
        blocJson = json.loads("".join(f.readlines()))
        
        ver = pack('<I', blocJson['blocks'][0]['ver']).encode('hex_codec')
        
        prev_nounce = blocJson['blocks'][0]['prev_block']
        prev_nounce = prev_nounce.decode('hex')[::-1].encode('hex_codec')
        
        mrkl_root = blocJson['blocks'][0]['mrkl_root']
        mrkl_root = mrkl_root.decode('hex')[::-1].encode('hex_codec')
        
        time = pack('<I', blocJson['blocks'][0]['time']).encode('hex_codec')
        
        nbits = pack('<I', blocJson['blocks'][0]['bits']).encode('hex_codec')
        
        nonce = pack('<I', blocJson['blocks'][0]['nonce']).encode('hex_codec') 
        
        header_hex = ver + prev_nounce + mrkl_root + time + nbits + nonce
        header_bin = header_hex.decode('hex')    
        #a=int('0x'+bloc, 0)
        return header_bin
    
header = lectureJson(125552)

hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
print(hexlify(hash).decode("utf-8"))
