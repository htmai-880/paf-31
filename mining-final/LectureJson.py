import json
from Sha256 import sha256

def lectureJson():
    with open("BlocBitcoin.json", "r") as f:        
        blocJson = json.loads("".join(f.readlines()))
        bloc=0
        bloc+=(blocJson['blocks'][0]['ver'])*2**(76*8)
        bloc+=int('0x'+blocJson['blocks'][0]['prev_block'],0)*2**(44*8)
        bloc+=int('0x'+blocJson['blocks'][0]['mrkl_root'],0)*2**(12*8)
        bloc+=(blocJson['blocks'][0]['time'])*2**(8*8)
        bloc+=(blocJson['blocks'][0]['bits'])*2**(4*8)
        bloc+=(blocJson['blocks'][0]['nonce'])
        print(bloc)
        #a=int('0x'+bloc, 0)
        return bloc
bloc=lectureJson()
res=hex(sha256(sha256(bloc)))

print(len(res))