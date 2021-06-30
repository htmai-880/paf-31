
from Sha256 import sha256
import random as rd
import string
import time
import numpy as np
import json
from multiprocessing import Pool

"""
length_block = 100
ints = string.digits
block = int('1'+''.join(rd.choice(ints) for _ in range(length_block)))
"""
def random_header():
    length_block = 76*8
    figures = '01'
    return int('0b1'+''.join(rd.choice(figures) for _ in range(length_block-1)), base = 0)



def mine(dif_target):
    t=time.perf_counter()
    #length_block = 1000
    #ints = string.digits
    block = random_header()
    #block = int('1'+''.join(rd.choice(ints) for _ in range(length_block)))
    nounce = 0
    while(nounce < 2**256):
        if pickaxe(nounce, block) <= dif_target:
            #print(nounce)
            temps = (time.perf_counter()-t)
            return nounce, temps
        nounce += 1
    return



#@jit(target ="cuda") 
def pickaxe(nounce, block):
    return sha256(sha256(block*2**32+nounce)) #typ='int'

if __name__ == "__main__":
    #d = int(input("Entrer le log2 du facteur de difficulté du bloc [0, 255]:\n"))
    #nounce, temps = mine(2**d)
    #print(nounce, temps)
    
    M = 2
    N = 3
    moyN = [0]*M
    moyT = [0]*M
    temps = [0]*257
    nounce = [0]*257
    ecartTypeTemps = [0]*257
    ecartTypeNounce = [0]*257
    MatT=np.zeros((N, M))
    MatN=np.zeros((N, M))
    
    args=[2**(255-i) for i in range(N) for j in range(M)]
    with Pool(5) as p:
        res=np.array(p.map(mine,args))
    MatT = res[:,1].reshape(N, M)
    MatN = res[:,0].reshape(N, M)
    temps = MatT.mean(axis=1)
    nounce = MatN.mean(axis=1)
    ecartTypeTemps = MatT.std(axis=1)
    ecartTypeNounce = MatN.std(axis=1)
    with open("Temps.json", "w") as ft:
        json.dump(temps.tolist(), ft)
    with open("Nounce.json", "w") as fn:
        json.dump(nounce.tolist(), fn)
    with open("EcartTypeTemps.json", "w") as fet:
        json.dump(ecartTypeTemps.tolist(), fet)
    with open("EcartTypeNounce.json", "w") as fen:
        json.dump(ecartTypeNounce.tolist(), fen)
