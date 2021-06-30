# paf-31
Fonction de hachage flexible


SBox : 
	On trouvera dans ce répertoire une implémentation python d'une fonction "Hadamard like".

sha2 :
	sha2.py est une implémentation python de la fonction de hachage cryptographique sha256
	compression.py contient l'étape de compression
	util.py contient l'implémentation de l'étape de bourrage et quelques fonctions utiles
	
	bitcoin_mining.py contient différentes fonctions pour simuler le minage de bitcoin à partir d'entêtes de blocs générés aléatoirement en utilisant les fonctions de hachage que nous avons réalisé
	
	LectureJson.py permet de reconstituer l'entête d'un bloc à partir des informations qui les constituent et de vérifier le haché annoncé dans la chaîne de bloc publique
	
mining-final :
	contient une version adaptée des algorithmes précédents pour les exécuter sur les GPU de l'école