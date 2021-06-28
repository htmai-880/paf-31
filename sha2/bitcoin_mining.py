import matplotlib.pyplot as plt
from sha2 import *
import random as rd
import string
import time
import numpy as np

length_block = 100
ints = string.digits
def_block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))

def mine(dif_target, block = def_block):
    nounce = 0
    while(nounce < 2**256):
        if pickaxe(nounce, block) <= dif_target:
            return nounce
        nounce += 1
    return

def pickaxe(nounce, block):
    return sha256(sha256(block*2**32+nounce, typ = 'int'), typ = 'int')

def mining_perf(dif_min, num_block):
    D = []
    c_list = []
    for dif_target in range(dif_min, 256):
        D.append(dif_target)
        for k in range(num_block):
            nounce_list = []
            block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))
            nounce_list.append(mine(2**dif_target, block))
##    for dif_target in range(dif_min, 2**255, 30):
##        D.append(dif_target)
##        mine(dif_target, int('1'+''.join(rd.choice(ints) for _ in range(length_block-1))))
        c_list.append(np.mean(nounce_list))
        
    plt.plot(D, c_list, 'o')
    plt.show()
        
def bitcoin_net(t, maj_num, duration_target):
    dif_list = []
    dif_list = []
    estimations_list = []
    prev_dif = 2**255
    for k in range(t):
        estimated_dif = 2**255

if __name__ == "__main__":
    d = int(input("Entrer le log2 du facteur de difficulté du bloc [0, 255]:\n"))
    mine(2**d)
