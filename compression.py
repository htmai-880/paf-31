import numpy as np


def bytexor(u, v):
    # u, v have the same size
    p = len(u)
    XOR_U_V = []
    for i in range(p):
        print(np.bitwise_xor(u[i], v[i]))
        XOR_U_V.append(int(np.bitwise_xor(u[i], v[i])))

    return bytearray(XOR_U_V)

def compression(chunk, hv):

    # hv is the hash value. hv[0] = hv0, ..., hv[7] = hv7.
    hv0 = hv[0]
    hv1 = hv[1]
    hv2 = hv[2]
    hv3 = hv[3]
    hv4 = hv[4]
    hv5 = hv[5]
    hv6 = hv[6]
    hv7 = hv[7]

    # chunk is a bytearray of 256 bits (32 bytes), cut in 8 words of 32 bits.
    a = chunk[0:4]
    b = chunk[4:8]
    c = chunk[8:12]
    d = chunk[12:16]
    e = chunk[16:20]
    f = chunk[20:24]
    g = chunk[24:28]
    h = chunk[28:32]





