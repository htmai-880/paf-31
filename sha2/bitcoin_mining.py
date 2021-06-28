import matplotlib.pyplot as plt
from sha2 import *
import random as rd
import string

ints = string.digits
block = int(''.join(rd.choice(ints) for _ in range(1000)))

def mine(dif_target):
    count = 0
    for nounce in range(1, 2**32-1):
        count += 1
        if pickaxe(nounce) <= dif_target:
            print(nounce)
            return count, nounce
    return

def pickaxe(nounce):
    return sha256(sha256(block*2**32+nounce, typ = 'int'), typ = 'int')

if __name__ == "__main__":
    d = int(input("Entrer le facteur de difficulté du bloc [0, 4294967295]:\n"))
    mine(d)
