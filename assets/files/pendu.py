# Le jeu du pendu
 
from tkinter import *
from random import choice
 
fichier = open("liste_mots.txt", "r")
liste_mots = fichier.readlines()    # met tous les mots du fichier dans une liste
fichier.close()


def lettre_dans_mot(lettre) :
    global partie_en_cours, mot_partiel, mot_choisi, nb_echecs, image_pendu
    if partie_en_cours : 
        nouveau_mot_partiel = ""
        lettre_dans_mot = False
        i=0
        while i<len(mot_choisi):
            if mot_choisi[i]==lettre:
                nouveau_mot_partiel = nouveau_mot_partiel + lettre
                lettre_dans_mot = True 
            else:
                nouveau_mot_partiel = nouveau_mot_partiel + mot_partiel[i]
            i+=1
        mot_partiel = nouveau_mot_partiel  
        afficher_mot(mot_partiel)
        if not lettre_dans_mot :        # lettre fausse. Changer le dessin.
            nb_echecs += 1
            nomFichier = "pendu_"+str(nb_echecs)+".gif"
            photo=PhotoImage(file=nomFichier)
            image_pendu.config(image=photo)
            image_pendu.image=photo
            if nb_echecs == 7:  # trop d'erreurs. Fini.
                partie_en_cours = False
                afficher_mot(mot_choisi)
        elif mot_partiel == mot_choisi:  # le mot a été trouvé !
            partie_en_cours = False
 

def afficher_mot(mot):
    global lettres
    mot_large = ""
    i=0
    while i<len(mot):  # ajoute un espace entre les lettres
        mot_large = mot_large + mot[i] + " "
        i+=1
    canevas.delete(lettres)
    lettres = canevas.create_text(320,60,text=mot_large,fill='black',font='Courrier 30') 

    
def init_jeu():
    global mot_choisi, mot_partiel, image_pendu, lettres
    global nb_echecs, partie_en_cours, liste_mots
    nb_echecs = 0
    partie_en_cours = True
    mot_choisi = choice(liste_mots).rstrip()
    mot_choisi = mot_choisi.upper()
    mot_partiel = "-" * len(mot_choisi)
    afficher_mot(mot_partiel)
    photo=PhotoImage(file="pendu_0.gif")
    image_pendu.config(image=photo)
    image_pendu.image=photo
        

# création du widget principal

fenetre = Tk()
fenetre.title("Le jeu du pendu")

canevas = Canvas(fenetre, bg='white', height=500, width=620)
canevas.pack(side=BOTTOM)

bouton = [0]*26
for i in range(26):
    bouton[i] = Button(fenetre,text=chr(i+65),command=lambda x=i+65:lettre_dans_mot(chr(x)))
    bouton[i].pack(side=LEFT)

bouton2 = Button(fenetre,text='Quitter',command=fenetre.quit)
bouton2.pack(side=RIGHT)
bouton1 = Button(fenetre,text='Recommencer',command=init_jeu)
bouton1.pack(side=RIGHT)

photo=PhotoImage(file="pendu_0.gif")
image_pendu = Label(canevas, image=photo, border=0)
image_pendu.place(x=120, y=140)
lettres = canevas.create_text(320,60,text="",fill='black',font='Courrier 30') 

init_jeu()

fenetre.mainloop()
fenetre.destroy()
               
