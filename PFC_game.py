from random import randint

#Tableau des options 
Jia  = ["pierre", "papier", "ciseaux"]

# option aléatoire à l'IA
Bots = Jia[randint(0,2)]

# les points du Joueur 1
Pointsjun = 0
# les points de l'IA
PointsBots = 0

continuer = True
print("Mode Classique")
#La boucle continue jusqu'à ce que la variable continuer est fausse
while(continuer):
    #Demander le choix 
    print("Vous Choisisez :")
    jun = input("pierre, papier, ciseaux? ou tapez FIN pour arrêter le jeu!\n")
    if(jun == 'FIN'):
        continuer = False
    elif(jun == Bots):
        print("Egalité!")
    elif(jun == "pierre"):
        if(Bots == "papier"):
            print("Tu a Perdu!", Bots, "recouvre", jun)
            PointsBots = PointsBots + 1 
        else:
            print("Tu a Gagné!", jun, "écrase", Bots)
            Pointsjun = Pointsjun + 1
    elif(jun == "papier"):
        if(Bots == "ciseaux"):
            print("Tu a Perdu!", Bots, "coupe", jun)
            PointsBots = PointsBots + 1 
        else:
            print("Tu a Gagné!", jun, "recouvre", Bots)
            Pointsjun = Pointsjun + 1
    elif(jun == "ciseaux"):
        if(Bots == "pierre"):
            print("Tu a Perdu!", Bots, "écrase", jun)
            PointsBots = PointsBots + 1
        else:
            print("Tu a Gagné!", jun, "coupe", Bots)
            Pointsjun = Pointsjun + 1
    else:
        print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    Bots = Jia[randint(0,2)]
    print('********Tour suivant********')

#Afficher les points
print("********Points********")
print("J1: ", Pointsjun)
print("IA: ", PointsBots)
