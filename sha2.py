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



h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

#32 bit word list
w0 = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
w = []
    
w = bytearray(w)

def sha256(message):
    message = bytearray(message, 'utf-8')

    ####Padding
    
    length = 8*len(message)
    message.append(0b1000000)

    zero_num = 7

    while (zero_num + length + 64 + 1)%512 != 0:
        zero_num+=8
        message.append(0x0)
    
    length_code = length.to_bytes(8, 'big')

    for byte in length_code:
        message.append(byte)

    ####Chunks processing

    chunk_list = [message[64*k:64*(k+1)] for k in range(len(message)//64)]

    w_list = [w.copy() for k in range(len(chunk_list))]

    for k in range(len(chunk_list)):
        w_list[k] = [int(byte) for byte in chunk_list[k].copy()]
        
    return message
