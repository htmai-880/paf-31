from math import log2
import numpy as np

def FHLVa(vectDep):
    taille = len(vectDep)
    tailleMoit = int(taille/2)
    log2Taille = int(log2(taille))
    H = np.array([[1, 1], [1, -1]])
    vectDepX = vectDep
    
    for j in range(log2Taille):
        Z=[]
        Y=[]
        for i in range(tailleMoit):
            X = (np.array([vectDepX[2*i], vectDepX[2*i+1]])).dot(H)  
            if i%2==1:
                Y.append(X[0])
                Z.append(X[1])
            else:
                Y=[X[0]]
                Z=[X[1]]

        vectDepX = [Y[0], Y[1], Z[0], Z[1]]
    return vectDepX
print(FHLVa([0, 1, 2, 3]))
