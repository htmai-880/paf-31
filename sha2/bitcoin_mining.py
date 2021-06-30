import matplotlib.pyplot as plt
from sha2 import *
import random as rd
import numpy as np
import time

length_block = 80//4
figures = '0123456789abcdef'
def_block = int('0x1'+''.join(rd.choice(figures) for _ in range(length_block)), base = 16)

def mine(dif_target, block = def_block):
    """Find the correct nounce for the block hash to be inferior to the difficulty target."""
    nounce = 0
    while(nounce < 2**256):
        if pickaxe(nounce, block) <= dif_target:
            return nounce
        nounce += 1
    return -1

def pickaxe(nounce, block):
    """Hash a block with a given nounce."""
    return sha256(sha256(block*2**32+nounce, typ = 'int'), typ = 'int')

def mining_perf(dif_min, num_block):
    """Plot the amount of nounces used before getting the correct hash, in function of the difficulty target."""
    dif_targets = []  # List of difficulty targets
    c_list = []  # List of count of nounces browsed to get the correct hash for a given difficulty target.
    for dif_target in range(dif_min, 256):
        dif_targets.append(dif_target)

        # Get the average count of nounces browsed to get the correct hash.
        for k in range(num_block):
            nounce_list = []
            block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))
            nounce_list.append(mine(2**dif_target, block))
        c_list.append(np.mean(nounce_list))
        
    plt.plot(dif_targets, c_list, 'o')
    plt.show()
        
def bitcoin_net(T, maj_num, duration_target):
    dif_list = [255]
    for t in range(T):
        dt_list = []
        for  block_num in range(maj_num):
            block = int('1'+''.join(rd.choice(ints) for _ in range(length_block-1)))
            real_t = time.perf_counter()
            mine(2**dif_list[t], block = block)
            if t >= T//2:
                mine(2**dif_list[t], block = block)
            dt_list.append(round((time.perf_counter()-real_t)*1000, 3))
            
        dif_list.append(np.log2(2**dif_list[t]*np.mean(dt_list)/(duration_target*maj_num)))
        
    plt.plot([t for t in range(T+1)], dif_list, '-')
    plt.show()

##if __name__ == "__main__":
##    d = int(input("Input log2 of the required difficulty target [0, 255]:\n"))
##    mine(2**d)
