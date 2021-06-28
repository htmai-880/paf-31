import matplotlib.pyplot as plt
from sha2 import *
import random as rd
import string
import time
import numpy as np

length_block = 1000
ints = string.digits
def_block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))

def mine(dif_target, block = def_block):
    nounce = 0
    while(nounce < 2**256):
        if pickaxe(nounce, block) <= dif_target:
            print(nounce)
            return nounce
        nounce += 1
    return

def pickaxe(nounce, block):
    return sha256(sha256(block*2**32+nounce, typ = 'int'), typ = 'int')

def mining_perf(dif_min, num_block):
    D = []
    t_list = []
    for dif_target in range(dif_min, 256):
        for k in range(num_block):
            dt = []
            block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))

            D.append(dif_target)
            t = time.perf_counter()
            mine(2**dif_target, block)
            dt.append(round((time.perf_counter()-t)*1000, 3))
            t_list.append(np.mean(dt))
        
    plt.plot(D, t_list, 'o')
    plt.show()
        

if __name__ == "__main__":
    d = int(input("Entrer le log2 du facteur de difficulté du bloc [0, 255]:\n"))
    mine(2**d)
