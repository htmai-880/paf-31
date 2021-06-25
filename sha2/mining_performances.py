import sha2
import matplotlib.pyplot as plt
import random as rd
import string

sha256 = sha2.sha256

block = ''.join(rd.choice(string.ascii_lowercase) for i in range(1000))
carac = string.printable

def mine(difficulty):
    nounce = ''
    count = 0
    for s0 in carac:
        for s1 in carac:
            for s2 in carac:
                for s3 in carac:
                    count+=1
                    nounce = s0+s1+s2+s3
                    if pickaxe(nounce) <= 2**32 - difficulty:
                        return count, nounce

def pickaxe(nounce):
    full_block = block + nounce
    return sha256(sha256(full_block))
