"""
This is the main algorithm
It calculates the hash vector
"""

from FHL import hachage
import time
import matplotlib.pyplot as plt

def SBox():
    # This is the size of symbPerm next line.
    # It has to be a power of 2, and >=4.
    nbSymb = int(input("Entrez le nombre de symboles (puissance de 2 >=4). Exemple : 16\n"))

    # If exception, we ask the user to correct
    while log2(nbSymb)!=int(log2(nbSymb)):
        print("Le nombre de symboles doit être une puissance de 2 >=4")
        nbSymb = int(input("Entrez le nombre de symboles (puissance de 2 >=4). Exemple : 16\n"))

    # This is the size if the vector the user inputs
    longDep = int(nbSymb/4)

    #We ask the user to input the vector to hash
    print("Entrez le vecteur de départ de taille ", longDep, ". Exemple : ", " ".join(f"{k:d}" for k in range(longDep)), sep = '', end = '')
    vectDep = [int(s) for s in input().split()]

    # If exception, we ask the user to correct
    while len(vectDep)!=longDep:
        print("Mauvaise longueur de vecteur")
        print("Entrez le vecteur de départ de taille ", longDep, ". Exemple : ", " ".join(f"{k:d}" for k in range(longDep)), sep = '', end = '')
        vectDep = [int(s) for s in input().split()]
     
    # This is the list of values that the elements of the hash vector can take
    symbPerm = [3*k%16 for k in range(nbSymb)]
    
    t=time.perf_counter()# We calculate the time
    
    vectSortie  = hachage(symbPerm, nbSymb, vectDep, longDep)
    
    print(round("Temps d'exécution :", (time.perf_counter()-t)*1000, 3), "ms")
    
    return vectSortie
    
#___________________________________________________________________________________________________________________________________________

vectSortie = SBox()

# Print of the hash vector in hexadecimal, and the time
print("\nVecteur haché : 0x"+ "".join(f"{elem:x}" for elem in vectSortie))

