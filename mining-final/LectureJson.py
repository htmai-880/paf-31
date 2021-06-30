import json

def lectureJson():
    with open("BlocBitcoin.json", "r") as f:        
        blocJson = json.loads("".join(f.readlines()))
        bloc=0
        bloc+=blocJson['blocks'][0]['ver']
        print(blocJson['blocks'][0])
lectureJson()