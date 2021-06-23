from util import *

'''
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19
hv = [h0, h1, h2, h3, h4, h5, h6, h7]

K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

W = [825307441, 808464432, 808464432, 808464432, 1077952576, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27140811487157147, 27140811470314138, 1111136037465961362162, 1111145083989107081600, 30948278999221517343583300, 30948502501603554415694190, 1267640305588583593774531304406, 1267650472400553513907299449988, 31154202817271152535786603429182532, 31153785201111447701676804799289094, 1276069320126815564861842897085472485785, 1276059011097026276498166159028097594666, 35542240461781840991418098886519397184876630, 35541817232465729543400965413223811177703874, 1455804556186383721022877562686563704967874235706, 1455792793901133622164738912443395423027344091766, 36058656219476671466086464508455785436060263602962499, 36058173071059013263503320594747885297516001525049091, 1476954572351201517301273098805703335022134828686494304374, 1476942733640337309637744737536839937606333800062866961138, 41137477527820215681135763361418982667920791087249960493799216, 41136991508247111260809875856482914230813069242322064926024470, 1684984639533504728795298563041425079554904263630861093154994660241, 1684971125914641636736854037483902495890412930557425173111110300716, 41410827956138185219861725712179868811449814764444240280357187508789131, 41411115334498431340060622435729217255901873349653632809122183887942711, 1696185339438200968219616223283800878850082428883205045558262039856718871883, 1696199243293613083884477052397816012020202951403224433844288044141867526476, 47243557302623278900702981669843270755310854648146375933694537230625005357920105, 47243899360086586278257918769033694177605541475647989943031230742736470376414995, 1935094204008654813273714036198548984569001218799093239154441337587640128581069887757, 1935109833113892298139613464891752176038715914271891363814675708522317054092122818556, 47929929658021231770384119780422078855800521296257946034698142070488074574738174348989296, 47930260675167119537808736579561520888521252933765459527683723454570337454272032506238705, 1963207446715477811841579428199085928270849723207735930643084365361382712694952091854977293231, 1963223430266154610998200707385924764609903036316680455248560764800430989004852888370386994738, 54680875909095696932430438861146896634743861248609105942689960200181563084438787548170128357445869, 54681270803624821721586228909672596330131595154887816996384061026655140500792965962053079410559629, 2239726553120893210119887499541951190568666504409983475464179721525460208261707383314793355546274045506, 2239744516322804561532652690664650052938834552706042868548251864323845476939907441614210909191013448652, 55044711803206007820126828322932359190438040824803181826784097404407919201640441059186051802092045200778837, 55043973939320028368144534161493201154325412176972628859762722984848659007242580049030931069433669668261101, 2254619332719812548038089093014666568222064967086731639020185242947301858907305854068769224720351359559711510093, 2254601118240788626983962051355396360014852352630339585099927662153554269376039248514765921363744447881745113180, 62797703235546772979912010510750982735435043136214058327602347295183556302598519232573693780065611391519361549362343, 62796955454071873492107680137359267518315235022280046024545889351622566292052633064928409896621066792657102485319962, 2572184006988910567738710476887903697935282302830043902591803610476359665007535941895891171336348443820020680525087531763, 2572163224829741333726095881271362826903958856999530948015499943033488809408786862619633552688443444884646097077655334964]
'''

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

    for j in range(8):
        hv[j] = (hv[j] + words[j]) % (2**32)


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
    temp1 = (h + S1 + ch_out + k[i] + w[i]) % (2**32)
    S0 = grandSigma0(a, bits)
    maj_out = maj(a, b, c)
    temp2 = (S0 + maj_out) % (2**32)

    words[7] = g
    words[6] = f
    words[5] = e
    words[4] = (d + temp1) % (2**32)
    words[3] = c
    words[2] = b
    words[1] = a
    words[0] = (temp1 + temp2) % (2**32)



