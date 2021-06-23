import random
from FHL import FHL
import time


nbSymb = int(input("Entrez le nombre de symboles. Exemple : 16\n"))


symbPerm = [random.randint(0, 16) for k in range(nbSymb)]
symbPerm.sort()


#symbPerm = [3, 15, 6, 5, 7, 13, 4, 8, 9, 1, 11, 10, 16, 12, 2, 14]
longDep = int(nbSymb/4)

print("Entrez le vecteur de départ de taille ", longDep, ". Exemple : ", " ".join(f"{k:d}" for k in range(longDep)), sep = '', end = '')

vectDep = [int(s) for s in input().split()]

t=time.perf_counter()

if len(vectDep)!=longDep:
    print("Mauvaise longueur de vecteur")
    exit
nouvVect = []
for i in range(longDep):
    j = (2*i+3)*vectDep[i] + i+1
    nouvVect.append(symbPerm[j%nbSymb])

vectSortie = [elem%nbSymb for elem in FHL(nouvVect)]
print(vectSortie)

print("\nVecteur de sortie : 0x"+ "".join(f"{elem:x}" for elem in vectSortie))
print("Temps d'exécution :", round((time.perf_counter()-t)*1000, 3), "ms")
