# Importer la librairie avec les commandes système
import os
print ("RG:Réperoire avant modif : "+ os.getcwd())
# Récuperer le repertoire du programme
basedir=(os.path.dirname(__file__))
# Afficher le répertoire
print ("RG:Réperoire du pgm .py : "+basedir)
# Changer le repertoire de travail (attention convertir en string avec str() )
path = os.chdir(str(basedir))
# Afficher le répertoire
print ("RG:Réperoire apres modif : "+os.getcwd())




