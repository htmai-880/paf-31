import numpy as np
import struct



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
    date_header, timestamp = struct.unpack('>BL', b)
    return timestamp


# ----------------------------------------------------------------------------------------------- #


def compression_loop(chunk, hv, i):
    # hv is the hash value. hv[0] = hv0, ..., hv[7] = hv7.
    hv0 = hv[0]
    hv1 = hv[1]
    hv2 = hv[2]
    hv3 = hv[3]
    hv4 = hv[4]
    hv5 = hv[5]
    hv6 = hv[6]
    hv7 = hv[7]

    # chunk is a bytearray of 512 bits (64 bytes), cut in 8 words of 32 bits.
    a = chunk[0:8]
    b = chunk[8:16]
    c = chunk[16:24]
    d = chunk[24:32]
    e = chunk[32:40]
    f = chunk[40:48]
    g = chunk[48:56]
    h = chunk[56:64]

    S1 = grandSigma1(0)


