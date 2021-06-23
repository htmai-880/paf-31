import random
from FHLVa import FHLVa
import time


nbSymb = 16
#X = (np.random.randn(1, NbSymboles)).sort()
symbPerm = [random.randint(0, 16) for k in range(nbSymb)]
symbPerm.sort()
longDep = 4

print("Entrez le vecteur de départ de taille 4. Exemple : 0 1 2 3")
vectDep = [int(s) for s in input().split()]

t=time.perf_counter()
#print(vectDep, len(vectDep), type(vectDep))
if len(vectDep)!=longDep:
    print("Mauvaise longueur de vecteur")
    exit
nouvVect = []
for i in range(longDep):
    j = (2*i+3)*vectDep[i] + i+1
    nouvVect.append(symbPerm[j%nbSymb])

vectSortie = [elem%nbSymb for elem in FHLVa(nouvVect)]

print("\nVecteur de sortie : 0x"+ "".join(f"{elem:x}" for elem in vectSortie))
print("Temps d'exécution :", round((time.perf_counter()-t)*1000, 3), "ms")
