"""
This is the main algorithm
It calculates the hash vector
"""


import random
from FHL import outVect
import time


# This is the size of symbPerm next line.
# It has to be a multiple of 4.
nbSymb = int(input("Entrez le nombre de symboles (multiple de 4). Exemple : 16\n"))

# If exception, we ask the user to correct
while nbSymb%4!=0:
    print("Le nombre de symboles doit être un multiple de 4")
    nbSymb = int(input("Entrez le nombre de symboles (multiple de 4). Exemple : 16\n"))

# _____________________________________________________________________________
    
# This is the list of values that the elements of the hash vector can take
# We chose to make this list random
symbPerm = [random.randint(0, 16) for k in range(nbSymb)] 
symbPerm.sort()

#symbPerm = [3, 15, 6, 5, 7, 13, 4, 8, 9, 1, 11, 10, 16, 12, 2, 14]

# _____________________________________________________________________________

# This is the size if the vector the user inputs
longDep = int(nbSymb/4)

print("Entrez le vecteur de départ de taille ", longDep, ". Exemple : ", " ".join(f"{k:d}" for k in range(longDep)), sep = '', end = '')
vectDep = [int(s) for s in input().split()]

# If exception, we ask the user to correct
while len(vectDep)!=longDep:
    print("Mauvaise longueur de vecteur")
    print("Entrez le vecteur de départ de taille ", longDep, ". Exemple : ", " ".join(f"{k:d}" for k in range(longDep)), sep = '', end = '')
    vectDep = [int(s) for s in input().split()]

# _____________________________________________________________________________
    
t=time.perf_counter() # We calculate the time the algorithm takes   
vectSortie  = outVect(symbPerm, nbSymb, vectDep, longDep) # Execution of the algorithm

# Print of the hash vector in hexadecimal, and the time
print("\nVecteur de sortie : 0x"+ "".join(f"{elem:x}" for elem in vectSortie))
print("Temps d'exécution :", round((time.perf_counter()-t)*1000, 3), "ms")

