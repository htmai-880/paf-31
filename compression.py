import numpy as np



#x est un mot et n est un entier, et length est le même que dans def sha256

def shr(x, n):
    return x>>n

def rotr(x, n, b):
    return x>>n | x<< (b - n)

def ch(x, y, z):
    return (x&y)^(~x&z)

def maj(x, y, z):
    return (x&y)^(x&z)^(y&z)

#bits = 32 ou 64

def grandSigma0(x, b):
    if b==32:
        return rotr(x, 2, b)^rotr(x, 13, b)^rotr(x, 22, b)
    else:
       return rotr(x, 28, b)^rotr(x, 34, b)^rotr(x, 39, b)

def grandSigma1(x, b):
    if b==32:
        return rotr(x, 6, b)^rotr(x, 11, b)^rotr(x, 25, b)
    else:
       return rotr(x, 14, b)^rotr(x, 18, b)^rotr(x, 41, b)

def petitSigma0(x, b):
    if b==32:
        return rotr(x, 7, b)^rotr(x, 18, b)^shr(x, 3)
    else:
       return rotr(x, 1, b)^rotr(x, 8, b)^shr(x, 7)

def petitSigma1(x, b):
    if b==32:
        return rotr(x, 17, b)^rotr(x, 19, b)^shr(x, 10)
    else:
       return rotr(x, 19, b)^rotr(x, 61, b)^shr(x, 6)

#=======================================================================================================#


def bytexor(u, v):
    # u, v have the same size
    p = len(u)
    XOR_U_V = []
    for i in range(p):
        print(np.bitwise_xor(u[i], v[i]))
        XOR_U_V.append(int(np.bitwise_xor(u[i], v[i])))

    return bytearray(XOR_U_V)

def compression_loop(chunk, hv):

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







