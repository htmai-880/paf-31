import matplotlib.pyplot as plt
from sha2 import *
import random as rd
import string
import time

length_block = 1000
ints = string.digits
block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))

def mine(dif_target):
    nounce = 0
    while(nounce < 2**256):
        if pickaxe(nounce) <= dif_target:
            print(nounce)
            return nounce
        nounce += 1
    return

def pickaxe(nounce):
    return sha256(sha256(block*2**32+nounce, typ = 'int'), typ = 'int')

def mining_perf(dif_min):
    D = []
    t_list = []
    for dif_target in range(dif_min, 256):
        D.append(dif_target)
        t = time.perf_counter()
        mine(2**dif_target)
        dt = round((time.perf_counter()-t)*1000, 3)
        t_list.append(dt)
    plt.plot(D, t_list, 'o')
    plt.show()
        

if __name__ == "__main__":
    d = int(input("Entrer le log2 du facteur de difficulté du bloc [0, 255]:\n"))
    mine(2**d)
