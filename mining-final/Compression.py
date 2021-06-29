from Util import grandSigma0, grandSigma1, ch, maj



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
    bits = 32
    words = [a, b, c, d, e, f, g, h]
    for i in range(64): #80
        compression_loop(words, k, w, i)

    for j in range(8):
        hv[j] = (hv[j] + words[j]) % (2**bits)

#@jit(target ="cuda") 
def compression_loop(words, k, w, i):
    ''' IN PLACE : changes array words'''
    # words is [a, b, c, d, e, f, g, h]

    a = words[0]
    b = words[1]
    c = words[2]
    d = words[3]
    e = words[4]
    f = words[5]
    g = words[6]
    h = words[7]

    bits = 32

    S1 = grandSigma1(e, bits)
    ch_out = ch(e, f, g)
    temp1 = (h + S1 + ch_out + k[i] + w[i]) % (2**bits)
    S0 = grandSigma0(a, bits)
    maj_out = maj(a, b, c)
    temp2 = (S0 + maj_out) % (2**bits)

    words[7] = g
    words[6] = f
    words[5] = e
    words[4] = (d + temp1) % (2**bits)
    words[3] = c
    words[2] = b
    words[1] = a
    words[0] = (temp1 + temp2) % (2**bits)