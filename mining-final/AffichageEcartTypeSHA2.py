import matplotlib.pyplot as plt
import numpy as np
import json

N=16

with open("Temps.json", "r") as f:        
    temps = json.loads("".join(f.readlines()))
with open("Nounce.json", "r") as f:        
    nounce = json.loads("".join(f.readlines()))
with open("EcartTypeTemps.json", "r") as f:        
    ecartTypeTemps = json.loads("".join(f.readlines()))
with open("EcartTypeNounce.json", "r") as f:        
    ecartTypeNounce = json.loads("".join(f.readlines()))

numbers_powers = [2**i for i in range(N)]

tempsPlus = [x + y for x, y in zip(temps, ecartTypeTemps)]
tempsMoins = [max(x - y, 0) for x, y in zip(temps, ecartTypeTemps)]

plt.figure("Temps")
plt.title("Temps d'exécution en fonction du facteur de difficulté\n pour un bloc de taille 1000")
axes = plt.gca()
axes.xaxis.set_ticks(numbers_powers)
plt.grid()

plt.plot(numbers_powers, tempsPlus, "c-.", label = "Ecart-type")
plt.plot(numbers_powers, tempsMoins, "c-.")
plt.plot(numbers_powers, temps, "r-+", label="Temps moyen", linewidth=3)
axes.xaxis.set_ticklabels(['0']+[' ' for k in range(1, 12)]+['2^'+str(k) for k in range(12,N)])
axes.yaxis.set_ticks(temps)
axes.yaxis.set_ticklabels(['0']+[' ' for k in range(1, 12)]+[round(temps[k]) for k in range(12,N)])

plt.legend()
#axes.set_ylim(0, 782)
plt.xlabel('Facteur de difficulté')
plt.ylabel('Temps d exécution en s')


nouncePlus = [x + y for x, y in zip(nounce, ecartTypeNounce)]
nounceMoins = [max(x - y, 0) for x, y in zip(nounce, ecartTypeNounce)]

plt.figure("Nounce")
plt.title("Nombre de nounces essayés en fonction du facteur de difficulté\n pour un bloc de taille 1000")
axes = plt.gca()
axes.xaxis.set_ticks(numbers_powers)
plt.grid()
plt.plot(numbers_powers, nouncePlus, "c-.", label = "Ecart-type")
plt.plot(numbers_powers, nounceMoins, "c-.")

plt.plot(numbers_powers, nounce, "r-+", label="Nombre de nounce moyen", linewidth=3)
axes.xaxis.set_ticklabels(['0']+[' ' for k in range(1, 12)]+['2^'+str(k) for k in range(12,N)])
axes.yaxis.set_ticks(nounce)
axes.yaxis.set_ticklabels(['0']+[' ' for k in range(1, 12)]+[round(nounce[k]) for k in range(12,N)])
plt.legend()
plt.xlabel('Facteur de difficulté')
plt.ylabel('Nombre de nounces essayés')
plt.show() 
