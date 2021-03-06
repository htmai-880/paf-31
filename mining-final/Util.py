import struct

# x est un mot et n est un entier, et length est le m?me que dans def sha256
#@jit(target ="cuda") 
def shr(x, n):
    return x >> n

#@jit(target ="cuda") 
def rotr(x, n, b):
    return x >> n | (x << (b - n) & (2 ** b - 1))

#@jit(target ="cuda") 
def ch(x, y, z):
    return (x & y) ^ (~x & z)

#@jit(target ="cuda") 
def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


# bits = 32 ou 64
#@jit(target ="cuda") 
def grandSigma0(x, b):
    if b == 32:
        return rotr(x, 2, b) ^ rotr(x, 13, b) ^ rotr(x, 22, b)
    else:
        return rotr(x, 28, b) ^ rotr(x, 34, b) ^ rotr(x, 39, b)

#@jit(target ="cuda") 
def grandSigma1(x, b):
    if b == 32:
        return rotr(x, 6, b) ^ rotr(x, 11, b) ^ rotr(x, 25, b)
    else:
        return rotr(x, 14, b) ^ rotr(x, 18, b) ^ rotr(x, 41, b)

#@jit(target ="cuda") 
def petitSigma0(x, b):
    if b == 32:
        return rotr(x, 7, b) ^ rotr(x, 18, b) ^ shr(x, 3)
    else:
        return rotr(x, 1, b) ^ rotr(x, 8, b) ^ shr(x, 7)

#@jit(target ="cuda") 
def petitSigma1(x, b):
    if b == 32:
        return rotr(x, 17, b) ^ rotr(x, 19, b) ^ shr(x, 10)
    else:
        return rotr(x, 19, b) ^ rotr(x, 61, b) ^ shr(x, 6)

#@jit(target ="cuda") 
def padding(bmessage):
    # bmessage is a message in bytearray
    """
    length = 16 * len(bmessage)
    bmessage.append(0b10000000)
    bmessage.append(0b000000000)
    zero_num = 15 #7"""
    length = 8 * len(bmessage)
    bmessage.append(0b10000000)
    zero_num = 7

    while (zero_num + length + 64 + 1) % 512 != 0: #128 1024
        zero_num += 8
        bmessage.append(0x0)

    #length_code = length.to_bytes(16, 'big')
    length_code = length.to_bytes(8, 'big')

    for byte in length_code:
        bmessage.append(byte)

#@jit(target ="cuda") 
def batoi(b):
    '''bytearray to integer'''
    # b is a bytearray
    var = struct.unpack('>L', b)
    return var[0]

#@jit(target ="cuda") 
def repr(ba):
    '''print bytearray'''
    s = ''
    for byte in ba:
        base = str(bin(byte))[2:]
        s += (8 - len(base)) * '0' + base + ' ' #16
    print(s)