#DEBUT
# definit la fonction random qui genere un nombre entre 1 et 3 
# definit la fonction input qui récupère les entrés joueur 
# inisialise la vaviable MenuDuJeux qui prend comme parametre" Mode Classique, Mode VS, ou Regle "

# assigner Mode Classique a la valeur 1
# assigner Mode VS a la valeur 2
# assigner Regle a la valeur 3
# MenuJ est egale a Vrai
# MJ est egale a Vrai

# definit la fonction JMenus qui prent comme parametre "MenuDuJeux"
    # afficher message "Bienvenue dans Pierre Feille Cisseaux"
    # attendre 1,5 seconde d'intervale 
    # afficher message "choisiser le Mode de jeux"
    # attendre 1,5 seconde d'intervale 
    # afficher message" Mode Classique, Mode VS, ou Regle "
    # assigner a la variable Jzero le retour de l'éxécution de la fonction input avec les paramètre " Mode Classique, Mode VS, ou Regle "
        #Tant que MenuJ est egale a Vrai
            #alors 
            # si Jzero est egale a 1
                #alors
                #assigner a ChoixMC le retour de l'éxécution de la fonction random qui prend comme parametre la valeur 1
                #return la fonction Jpartie avec les paramètre Jzero et ChoixMC
                #remplacez dans MenuJ Vrai par Faux
            #sinon si Jzero est égale a 2
                #alors
                #assigner a ChoixVS le retour de l'éxécution de la fonction random qui prend comme parametre la valeur 2
                #return la fonction Jpartie avec les paramètre Jzero et ChoixVS
                #remplacez dans MenuJ Vrai par Faux
            #sinon si Jzero est égale a 3
                #alors
                #assigner a ChoixRegle le retour de l'éxécution de la fonction random qui prend comme parametre la valeur 2
                #return la fonction JRegle avec les paramètre Jzero et ChoixRegle
            #sinon
                #alors 
                # affiche message d'erreur "une erreur est aparue veiliez réessayer !",
                # afficher message "choisiser le Mode de jeux"



# definir la fonction Jpartie avec les paramètre Jzero et ChoixMC
    # assigner a la variable Jun le retour de l'éxécution de la fonction input avec les paramètre (Pierre, Feille, et Cisseaux)
    # redefinir la fonction random qui importeras la fonction integré randint qui genere un nombre aleatoire entre 1 et 3 
    # Atribuer a IA la fonction random qui va genere un nombre aléatoire entre 1 et 3
    # assigner Pierre a la valeur 1
    # assigner Feille a la valeur 2
    # assigner Cisseaux a la valeur 3
    # Afficher message : "que la partie commence"
    # attendre 2 seconde d'intervale
    # Tant que MJ est egale a Vrai
        # Alors afficher message :  "choisiser entre : (1)Pierre (2)Feille ou (3)Cisseaux."
        # SI Jun est egale a IA
            #Alors afficher message : "Egalité !"
        # SINON SI Jun est egale 1
            # IA est egale 2 
            # Alors Afficher message : 2 "gagne contre" 1 
            # Afficher message : "Vous avez Perdu ! Victoire de l'IA !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 1
            #  IA est egale a 3
            # Alors Afficher message : 1 "gagne contre" 3
            # Afficher message : "Vous avez Gagier ! Victoire du Joueur !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 2
            #  IA est egale a 3
            # Alors Afficher message : 2 "gagne contre" 3
            # Afficher message : "Vous avez Perdu ! Victoire de l'IA !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 2
            #  IA est egale a 1
            # Alors Afficher message : 2 "gagne contre" 1
            # Afficher message : "Vous avez Gagier ! Victoire du Joueur !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 3
            #  IA est egale a 1
            # Alors Afficher message : 1 "gagne contre" 3
            # Afficher message : "Vous avez Perdu ! Victoire de l'IA !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 3
            #  IA est egale a 2
            # Alors Afficher message : 3 "gagne contre" 2
            # Afficher message : "Vous avez Gagier ! Victoire du Joueur !"
            # remplacer dans MJ VRAI par FAUX
        # SINON 
            # Alors affiche message d'erreur "une erreur est aparue veiliez réessayer !"
            # Afficher message :  "choisiser entre : (1)Pierre (2)Feille ou (3)Cisseaux."
    # attendre 3 seconde d'intervale
    # retour vers la fonction JMenus 

    
# definir la fonction Jpartie avec les paramètre Jzero et ChoixVS
# assigner a la variable Jun le retour de l'éxécution de la fonction input avec les paramètre (Pierre, Feille, et Cisseaux)
# assigner a la variable Jdeux le retour de l'éxécution de la fonction input avec les paramètre (Pierre, Feille, et Cisseaux)
    # assigner Pierre a la valeur 1
    # assigner Feille a la valeur 2
    # assigner Cisseaux a la valeur 3
    # Afficher message : "que la partie commence"
    # attendre 2 seconde d'intervale
    # Tant que MJ est egale a Vrai
        # Alors afficher message :  "choisiser entre : (1)Pierre (2)Feille ou (3)Cisseaux."
        # SI Jun est egale a Jdeux
            #Alors afficher message : "Egalité !"
        # SINON SI Jun est egale 1
            # Jdeux est egale 2 
            # Alors Afficher message : 2 "gagne contre" 1 
            # Afficher message : "Victoire de J2 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 1
            #  Jdeux est egale a 3
            # Alors Afficher message : 1 "gagne contre" 3
            # Afficher message : "Victoire de J1 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 2
            #  Jdeux est egale a 3
            # Alors Afficher message : 2 "gagne contre" 3
            # Afficher message : "Victoire de J2 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 2
            #  Jdeux est egale a 1
            # Alors Afficher message : 2 "gagne contre" 1
            # Afficher message : "Victoire de J1 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 3
            #  Jdeux est egale a 1
            # Alors Afficher message : 1 "gagne contre" 3
            # Afficher message : "Victoire de J2 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON SI Jun est egale 3
            #  Jdeux est egale a 2
            # Alors Afficher message : 3 "gagne contre" 2
            # Afficher message : "Victoire de J1 !"
            # remplacer dans MJ VRAI par FAUX
        # SINON 
            # Alors affiche message d'erreur "une erreur est aparue veiliez réessayer !"
            # Afficher message :  "choisiser entre : (1)Pierre (2)Feille ou (3)Cisseaux."
    # attendre 3 seconde d'intervale
    # retour vers la fonction JMenus


# definir fonction JRegle avec comme paramètre Jzero et ChoixRegle
    # affiché message "voici les regles du pierre feille cisseaux.
    # Le jeux ce joue seul en Mode Classique ou a deux en Mode VS.
    # le jeux possède trois objets: la Pierre, la Feille et les Cisseaux.
    # La logique du jeux veux que :
    # la Feille gagne contre la Pierre, les Cisseaux gagne contre la Feille, et que la Pierre gagne contre les Cisseaux.
    # Au debut de la partie tu a un choix a faire entre pierre, feille ou cisseaux
    # une fois que tu a choisie l'IA(mode classique) ou le deuxième joueurs(mode VS) doit choisie a son tour.
    # le joueur qui possède l'objet le plus forte pendant cette partie l'emporte 
    # attendre 5 seconde d'intervale
    # si tu a compris les regles alors bon jeux a toi !"
    # attendre 3 seconde d'intervale
    # #retour vers la fonction JMenus

#FIN
