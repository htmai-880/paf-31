import numpy as np
import struct
from util import *


# ----------------------------------------------------------------------------------------------- #


def bytexor(u, v):
    # u, v have the same size
    p = len(u)
    XOR_U_V = []
    for i in range(p):
        print(np.bitwise_xor(u[i], v[i]))
        XOR_U_V.append(int(np.bitwise_xor(u[i], v[i])))

    return bytearray(XOR_U_V)


def batoi(b):
    '''bytearray to integer'''
    # b is a bytearray
    var = struct.unpack('>L', b)
    return var[0]

# ----------------------------------------------------------------------------------------------- #

def process(hv, k, w):
    # hv is the hash value. hv[0] = hv0, ..., hv[7] = hv7.
    a = hv[0]
    b = hv[1]
    c = hv[2]
    d = hv[3]
    e = hv[4]
    f = hv[5]
    g = hv[6]
    h = hv[7]

    words = [a, b, c, d, e, f, g, h]
    for i in range(64):
        compression_loop(words, k, w, i)

    hv[0] += words[0]
    hv[1] += words[1]
    hv[2] += words[2]
    hv[3] += words[3]
    hv[4] += words[4]
    hv[5] += words[5]
    hv[6] += words[6]
    hv[7] += words[7]


def compression_loop(words, k, w, i):
    ''' IN PLACE : changes array words'''
    # words = [a, b, c, d, e, f, g, h]
    a = words[0]
    b = words[1]
    c = words[2]
    d = words[3]
    e = words[4]
    f = words[5]
    g = words[6]
    h = words[7]

    b = 32

    S1 = grandSigma1(e, b)
    ch_out = ch(e, f, g)
    temp1 = (h + S1 + ch_out + k[i] + w[i]) % (2**32)
    S0 = grandSigma0(a, b)
    maj_out = maj(a, b, c)
    temp2 = S0 + maj_out

    words[7] = g
    words[6] = f
    words[5] = e
    words[4] = d + temp1
    words[3] = c
    words[2] = b
    words[1] = a
    words[0] = temp1 + temp2




