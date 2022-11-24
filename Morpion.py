#importer la bibliothéque time
import time
from math import inf as infinity
from random import choice
import platform
import time
from os import system


#dictionnaire associant une valeur à chaque symbole
valeur = {' ':0,'O':3,'X':5}

#definir la fonction ecriture_possible qui retourne comme parametre grille et chaine
def ecriture_possible(grille,chaine):
    # assigner pos a Faux
    pos = False
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    lig = int(chaine[0])
    # assigner col a int qui contient le tableu chaine avec l'index 1
    col = int(chaine[1])
    # Si le tableau grille contenant lig et col est egale a aucune valeur
    if grille[lig][col] == ' ':
        #Alors pos est egale a VRAI 
        pos = True
        #retourné pos
    return pos

#definir la fonction ecriture qui retourne comme parametre grille,chaine et symbole 
def ecriture(grille,chaine,symbole):
    # assigner lig a int qui contient le tableu chaine avec l'index 0
    ligne = int(chaine[0])
    # assigner col a int qui contient le tableu chaine avec l'index 1
    colonne=int(chaine[1])
    #Assigne le tableau grille contenant ligne et colonne a symbole 
    grille[ligne][colonne]=symbole
    #Retourné le tableau grille 
    return grille

#definir la fonction alignement_ligne qui retourne comme parametre grille
def alignement_ligne(grille):
    # Assigner aligne a la valeur 0 
    aligne = 0
    # Pour chaque i ranger en 3 
    for i in range(3):
        #assigier somme a la valeur 0
        somme = 0
        #Pour chaque J ranger en 3 
        for j in range(3):
            #assigner symbole aux tableau grille avec ses parametre i et J
            symbole = grille[i][j]
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
            somme = somme + valeur[symbole]
        #SI somme est egale a la valeur 15 ou a la valeur 9 
        if somme == 15 or somme == 9 :
            #alors assigne alige a la valeur 1 
            aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_colonne qui vas retoiurné comme parametre grille
def alignement_colonne(grille):
    #alors assigne alige a la valeur 0
    aligne = 0
    #Pour chaque J ranger en 3
    for j in range(3):
        #assigne somme a la valeur 0 
        somme = 0
        #pour chaque i ranger en 3 
        for i in range(3):
            #assigner symbole aux tableau grille avec ses parametre i et J
            symbole = grille[i][j]
            #assigner somme a somme plus au tableau valeur avec symbole dedans 
            somme = somme + valeur[symbole]
        #SI somme est egale a la valeur 15 ou a la valeur 9 
        if somme == 15 or somme == 9 :
            #alors assigne alige a la valeur 1 
            aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_diag1 qui vas retoiurné comme parametre grille
def alignement_diag1(grille):
    #Assigner aligne a la valeur 0 
    aligne = 0
    #Assigier somme a la valeur 0
    somme = 0
    #pour chaque i ranger en 3 
    for i in range(3):
        #assigner symbole aux tableau grille avec ses parametre i et i
        symbole = grille[i][i]
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
        somme = somme + valeur[symbole]
    #SI somme est egale a la valeur 15 ou a la valeur 9 
    if somme == 15 or somme == 9 :
        #alors assigne alige a la valeur 1 
        aligne = 1
    #retourné aligne 
    return aligne

#definir alignement_diag1 qui vas retoiurné comme parametre grille
def alignement_diag2(grille):
    #Assigner aligne a la valeur 0 
    aligne = 0
    #Assigier somme a la valeur 0
    somme = 0
    #pour chaque i ranger en 3 
    for i in range(3):
        #assigner symbole aux tableau grille avec ses parametre i et 2 - i
        symbole = grille[i][2-i]
        #assigner somme a somme plus au tableau valeur avec symbole dedans 
        somme = somme + valeur[symbole]
    #SI somme est egale a la valeur 15 ou a la valeur 9 
    if somme == 15 or somme == 9 :
        #alors assigne alige a la valeur 1 
        aligne = 1
    #retourné aligne 
    return aligne

#definir alignement qui vas retoiurné comme parametre grille
def alignement(grille):
    # assigner aligne a alignement_ligne + alignement_colonne
    # + alignement_diag1 + alignement_diag2 qui possède tous le parametre grille
    aligne = alignement_ligne(grille)+alignement_colonne(grille)+alignement_diag1(grille)+alignement_diag2(grille)
    #SI aligne est egale a 1 
    if aligne == 1 :
        #alors afficher message  "trois symboles alignés! le jeu est fini."
        print("trois symboles alignés! le jeu est fini.")
        #retourné VRAI 
        return True
    #Sinon
    else :
        #retourné Faux 
        return False


    #################################################    corps du programme    #################################################
def JcJ():

    #construction d'une grille vide
    grille= []
    #pour chaque i ranger en 3 
    for i in range(3):
        #inisialiser ligne au tabeau
        ligne=[]
        #pour chaque j ranger en 3 
        for j in range(3):
            #ajouté append a ligne qui retourne rien
            ligne.append(' ')
        #ajouté append a grille qui retourne ligne
        grille.append(ligne)
    # assigner le joueurs a chaque symbole
    joueur = {0:'O',1:'X'}


    #assigner tour a la valeur 0
    tour = 0
    compteTour = 0
    # fin est egale Faux
    fin = False
    #Tant que c'est pas egale a fin 
    while not fin :
        #alors correct est egale a FAUX
        correct = False
        #Tant que c'est pas egale a correct :
        while not correct :
            # assigner a la variable rep le retour de l'éxécution de la fonction input avec le message "Quelle case souhaitez-vous cocher ?\n"
            rep = input("Quelle case souhaitez-vous cocher ?\n")
            if not rep in ["00","01","02","10","11","12","20","21","22"]:
                print("veuillez ressaisir la demande")
            elif rep in ["00","01","02","10","11","12","20","21","22"]:
                # assigner la valeur correct a la fonctionecriture_possible qui retourne grille et rep
                correct = ecriture_possible(grille,rep)     
        # assigner dessin aux parametre joueur qui retourne "tour"
        dessin = joueur[tour]
        # assigner grille a la fonction ecriture qui retourne "grille, rep et dessin"
        grille = ecriture(grille,rep,dessin)
        #pour chaque i ranger en 3 
        for i in range(3):
            #afficher le message du parametre grille i
            print(grille[i])
        # assigner a la variable fin a la fonction alignement qui retourne "grille"
        fin = alignement(grille)
        #ajouté +1 a tour
        tour = (tour + 1)%2
        #ajouté +1 a comptetour 
        compteTour = compteTour + 1
        #Si compteTour est egale a 9 
        if compteTour == 9 :
            #alors affiché message : egalité 
            print("égalité")
            #appeler la fonction exit
            exit()
            
#Definir la fonction JcIA
def JcIA():
    #assiger J a la valeur -1
    J = -1
    #assiger IA a la valeur +1
    IA = +1
    #affiché un tableau nommé board 
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    #definir la focton evaluate qui retourne comme parametre state
    def evaluate(state):
        #Si la fonction wins prend les parametre state et la valeur IA 
        if wins(state, IA):
            #alors assiger la variable score a la valeur +1 
            score = +1
        #Sinon Si la fonction wins prend les parametre state et J
        elif wins(state, J):
            #alors assiger la variable score a la valeur -1
            score = -1
        #Sinon 
        else:
            #alors la variable score est egale a 0 
            score = 0
        #retouré la variable score 
        return score

    #definir la fonction wins qui retourne comme parametre state et player 
    def wins(state, player):
        # affiché une liste nommé win_state
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        #Si 
        if [player, player, player] in win_state:
            #alors retourne 
            return True
        #sinon
        else:
            #alors retourné faux 
            return False

    #definir la fonction game_over qui prent comme parametre state
    def game_over(state):
        #retourné la fonction wins qui prent comme parametre state et J ou la fonction wins qui prent comme parametre state et IA
        return wins(state, J) or wins(state, IA)

    #definir la fonction empty_cells qui prent comme parametre state
    def empty_cells(state):
        
        cells = []
        #pour chaque x et row dans la fonction enumerate qui prend comme parametre state
        for x, row in enumerate(state):
            #pour chaque y et cell dans la fonction enumerate qui prend comme parametre row 
            for y, cell in enumerate(row):
                #Si cell est égale a 0 
                if cell == 0:
                    #alors appeler cells append([x, y])
                    cells.append([x, y])

        #retourné cells 
        return cells

    #definir la fonction valid_move qui a pour parametre x et y 
    def valid_move(x, y):
        #Si la liste x et y est dans la foction empty_cells qui a comme parametre board 
        if [x, y] in empty_cells(board):
            #alors retourné vrai 
            return True
        #sinon
        else:
            #alors retourné faux 
            return False

    #definir la fonction set_move qui prend comme parametre x, y et player
    def set_move(x, y, player):
        #Si la fonction valid_move a pour parametre x et y 
        if valid_move(x, y):
            #alors on assigne le tableau board x y a la variable player
            board[x][y] = player
            #retourné vrai 
            return True
        #sinon 
        else:
            #retourné faux 
            return False

    #definir la fonction minimax qui prend comme parametre state, depth et player
    def minimax(state, depth, player):
        #Si player est egale a l'IA 
        if player == IA:
            #alors assiger la liste best [-1, -1, -infinity]
            best = [-1, -1, -infinity]
        #Sinon
        else:
            #alors assiger la liste best [-1, -1, +infinity]
            best = [-1, -1, +infinity]
        #Si depth est égale a la valeur 0 ou a la fonction game_over qui retourne comme parametre state 
        if depth == 0 or game_over(state):
            #alors score est égales evaluate(state) 
            score = evaluate(state)
            #retourné la liste [-1, -1, score]
            return [-1, -1, score]
        #pour chaque celle dans la fonction 
        for cell in empty_cells(state):
            #x et y est égale a cell[0], cell[1]
            x, y = cell[0], cell[1]
            # assigner player aux paramètre state [x][y]
            state[x][y] = player
            #assigne score a la foction minimax qui prens comme parametre state, depth - 1 et -player
            score = minimax(state, depth - 1, -player)
            # assigne state[x][y] a la valeur 0
            state[x][y] = 0
            #score[0] et scrore[1] est egale a x, y
            score[0], score[1] = x, y

            #si player est egale a IA : 
            if player == IA:
                #si scrore[2] est suprérieur a best[2]
                if score[2] > best[2]:
                    #alors best est égale a score 
                    best = score  # max value
            #sinon 
            else:
                #Si score[2] est supérieur a best[2]
                if score[2] < best[2]:
                    #alors best est égale a score 
                    best = score  # min value
        #retourné best 
        return best

    #definir la fonction clean()
    def clean():
        #os_name est egale a platform.system().lower()
        os_name = platform.system().lower()
        #Si windows est dans la variable os_name
        if 'windows' in os_name:
            #alors apeler la fonction system qui retourne le message 'cls'
            system('cls')
            #sinon
        else:
            #alors apeler la fonction system qui retourne le message 'clear'
            system('clear')
            
    #definir la fonction render (state, c_choice)
    def render(state, c_choice, h_choice): 
        #chars est egale a une liste h_choice, c_choice et ''.
        chars = {
            -1: h_choice,
            +1: c_choice,
            0: ' '
        }
        str_line = '---------------'

        #affiché un message ('\n' + str_line)
        print('\n' + str_line)
        #pour chaque row dans state 
        for row in state:
            #pour chaque cell danns row 
            for cell in row:
                #assiger symbole a chars[cell]
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    #definir la fonction ia_turn qui prend comme parametre c_choice, h_choice
    def ia_turn(c_choice, h_choice):
        #assigner depth a la fonction len qui prend comme parametre empty_cells(board)
        depth = len(empty_cells(board))
        #si  depth est egale a 0 or a game_over avec les parametre board
        if depth == 0 or game_over(board):
            #retourné la fonction 
            return

        #appeler la fonction clean()
        clean()
        #affiché message f'IA Joue [{c_choice}]'
        print(f'IA Joue [{c_choice}]')
        #appeler la fonction render avec les parametres board, c_choice et h_choice
        render(board, c_choice, h_choice)

        #si depth est egale a la valeur 9 
        if depth == 9:
            #alors x est egale a la fonction choice avec les valeurs [0, 1, 2]
            x = choice([0, 1, 2])
            #alors y est egale a la fonction choice avec les valeurs [0, 1, 2]
            y = choice([0, 1, 2])
        #sinon
        else:
            #assiger move a minimax avec les parametre board, depth et l'IA
            move = minimax(board, depth, IA)
            #assiger x, y a move [0] et move[1]
            x, y = move[0], move[1]
        #appeler la fonction set_move avec les parametres x, y et IA
        set_move(x, y, IA)
        #ajouté 1 a time.sleep
        time.sleep(1)

    #definir la fonction human_turn qui prend comme parametre c_choice et  h_choice
    def human_turn(c_choice, h_choice):
        #assiger depth a la fonction len qui retoune comme parmetre la fonction empty_cells(board)
        depth = len(empty_cells(board))
        #si depth est égale a 0 ou a la fonction game_over qui retourne les parametre board
        if depth == 0 or game_over(board):
            #alros retourne la fonction 
            return

        # ajouté un Dictionaire des moves possible 
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }
        #appeler la fonction clean()
        clean()
        #affiché message "A vous de jouer [{c_choice}]"
        print(f'A vous de jouer [{h_choice}]')
        #appeler la fonction render avec les parametres board, c_choice et h_choice
        render(board, c_choice, h_choice)

        #tant que mouve est inferieur a 1 ou supérieur a 9 
        while move < 1 or move > 9:
            #alors 
            try:
                #assiger mouve a int qui a comme parametre la fonction input et un message 'numéro ? (1..9): '
                move = int(input('numéro ? (1..9): '))
                #assiger coord a mouves[move]
                coord = moves[move]
                #assigner can_mouve a la fonction set_move avec les parametre (coord[0], coord[1] et J)
                can_move = set_move(coord[0], coord[1], J)

                #Si c'est pas égale a la variavle can_move 
                if not can_move:
                    #alors affiche un message 'mauvaise saisis'
                    print('mauvaise saisis')
                    #assigne move a la valeur -1 
                    move = -1
            #appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
            except (EOFError, KeyboardInterrupt):
                #affiche message 'adieu'
                print('Adieu')
                #fermé la fonction 
                exit()
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
            except (KeyError, ValueError):
                #affiche message 'Mauvais choix'
                print('Mauvais choix')

    #definir la fonction main
    def main():
        #appeler la fonction clean()
        clean()
        h_choice = ''  # X or O
        c_choice = ''  # X or O
        first = ''  # if human is the first

        #tant que h_choice est non egale aux message 'O' et non egale aux message 'X'
        while h_choice != 'O' and h_choice != 'X':
            #alors
            try:
                #affiche aucun message 
                print('')
                #assigne h_choice aux retoure de l'execution de la fonction input 'Choisit X ou O\nChoix : ' avec la fonction upper()
                h_choice = input('Choisit X ou O\nChoix : ').upper()
            # appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
            except (EOFError, KeyboardInterrupt):
                #affiche message 'adieu'
                print('Adieu')
                #fermé la fonction 
                exit()
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
            except (KeyError, ValueError):
                #affiche message 'Mauvais choix'
                print('Mauvais choix')

        #Si h_choice est égale a X,
        if h_choice == 'X':
            #alors c_choice est égale a O
            c_choice = 'O'
            #sinon
        else:
            #c_choice est egale a X
            c_choice = 'X'

        #appeler la fonction clean()
        clean()
        #tant que la variable first est non egale a'Y' et est non egale a N
        while first != 'Y' and first != 'N':
            #alors 
            try:
                #assigner la variable first aux retour de l'execution dela fonction input qui retoure le message 'Tu veux commencer ?[y/n]: ' avec la fonction upper()
                first = input('Tu veux commencer ?[y/n]: ').upper()
            # appeler la fonction except qui prent comme parametre EOFError et KeyboardInterrupt
            except (EOFError, KeyboardInterrupt):
                #affiche message 'adieu'
                print('Adieu')
                #fermé la fonction 
                exit()
            #appeler la fonction except qui prent comme parametre KeyError et ValueError
            except (KeyError, ValueError):
                #affiche message 'Mauvais choix'
                print('Mauvais choix')

        #tant que len avec ses parametre empty_cells(board) est supérieur a 0 et non a game_over(board)
        while len(empty_cells(board)) > 0 and not game_over(board):
            #si first est égale a N
            if first == 'N':
                #alors appeller la foncion ia_turn avecles parametres c_choice, h_choice
                ia_turn(c_choice, h_choice)
                #assigner first a rien 
                first = ''

            #appeller la foncion human_turn avec les parametres c_choice et h_choice
            human_turn(c_choice, h_choice)
            #appeller la foncion ia_turn avec les parametres c_choice et h_choice
            ia_turn(c_choice, h_choice)

        # Game over message
        #Si la fonction wins a pour parametres board et J
        if wins(board, J):
            #Alors #appeler la fonction clean()
            clean()
            #affiché le message 'A toi de jouer[{h_choice}]'
            print(f'A toi de jouer[{h_choice}]')
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            render(board, c_choice, h_choice)
            #affiché le message 'TU AS GAGNER!'
            print('TU AS GAGNER!')
        #sinon si la fonction wins a pour parametres board et IA
        elif wins(board, IA):
            #alors #appeler la fonction clean()
            clean()
            #affiché le message 'IA joue [{c_choice}]'
            print(f'IA joue [{c_choice}]')
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            render(board, c_choice, h_choice)
            #affiché le message 'TU AS PERDU !'
            print('TU AS PERDU !')
        #sinon
        else:
            #alors #appeler la fonction clean()
            clean()
            #appeler la foncton render qui a comme parametres board, c_choice et  h_choice
            render(board, c_choice, h_choice)
            #affiché le message 'egalité !'
            print('EGALITE !')
        #fermé la fonction 
        exit()


    if __name__ == '__main__':
        main()


#################################################    Regle du morpion    ################################################# 

#definir la fonction regle_morpion
def regle_morpion() :
    #affiché message "Bienvenue sur ce Morpion de qualité !\n"
    print("Bienvenue sur ce Morpion de qualité !\n")
    #affiché un espace 
    print(" \n")
    # affiché message "Je suis Morpious votre serviteur et guide sur ce morpion. Pour commencer, ce morpion fut créé par Kyllian et William. Mes 2 géniaux créateur.
    # Ce Morpion vous propose une version joueur contre joueur et une version contre moi ! (attention je suis imbattable à ce jeu).\n"
    print("Je suis Morpious votre serviteur et guide sur ce morpion. Pour commencer, ce morpion fut créé par Kyllian et William. Mes 2 géniaux créateur. Ce Morpion vous propose une version joueur contre joueur et une version contre moi ! (attention je suis imbattable à ce jeu).\n")
    #affiché un espace 
    print(" \n")
    #affiché message "Les règles sont simple : \n"
    print("Les règles sont simple : \n")
    #affiché message "Le tableau est diviser un 9 cases. Ces 9 cases sont présentes sur des lignes et des colonnes nominées de 0 à 2.
    #Pour afficher l’un de vos symboles ( X ou O) vous devrais mettre votre réponses sous cette forme: ligne – colonne (sans le tiré). \n"
    print("Le tableau est diviser un 9 cases. Ces 9 cases sont présentes sur des lignes et des colonnes nominées de 0 à 2. Pour 	afficher l’un de vos symboles ( X ou O) vous devrais mettre votre réponses sous cette forme: ligne – colonne (sans le tiré). \n")
    #affiché message "Par exemple si vous souhaité mettre votre symbole au milieux vous devrait taper : 11 (1 = ligne, 1 = colonne)\n"
    print("Par exemple si vous souhaité mettre votre symbole au milieux vous devrait taper : 11 (1 = ligne, 1 = colonne)\n")
    #affiché message "Si vous souhaité mettre votre symbole en haut a droite vous devrait taper : 02 (0 = ligne, 2 = colonne)\n"
    print("Si vous souhaité mettre votre symbole en haut a droite vous devrait taper : 02 (0 = ligne, 2 = colonne)\n")
    #affiché message "/!\  Aucune triche n’est autorisé de ta part  /!\ \n"
    print("/!\  Aucune triche n’est autorisé de ta part  /!\ \n")
    #affiché message "Le premier à aligner 3 symboles gagne la partie ! \n"
    print("Le premier à aligner 3 symboles gagne la partie ! \n")
    #affiché un espace
    print(" \n")
    #affiché message " Tu es prés ?\n"
    print(" Tu es prés ?\n")
    #assiger mode au retoure de la fonction input qui affiche le message " Appuis envoie donc 1 pour jouer en Joueur contre Joueur ou 2 pour jouer contre Moi (IA)\n"
    mode = input(" Appuis envoie donc 1 pour jouer en Joueur contre Joueur ou 2 pour jouer contre Moi (IA)\n")
    #Si mode est égale a 1 
    if mode == "1":
        #Alors affiché message "Félicitation vous avez choisi de jouer entre vous j'espere qu'apres cette partie votre amitié sera toujours intacte <3 "
        print ("Félicitation vous avez choisi de jouer entre vous j'espere qu'apres cette partie votre amitié sera toujours intacte <3 ")
        #ajouté 2 a time.sleep
        time.sleep (2)
        #appeler la fonction JcJ()
        JcJ()
    #sinon si mode est egale a 2
    elif mode == "2":
        #alors affiché message "Félicitation vous avez choisi de jouer contre moi je vais te briser ! "
        print ("Félicitation vous avez choisi de jouer contre moi je vais te briser ! ")
        #ajouté 2 a time.sleep
        time.sleep (2)
        #appeler la fonction JcIA()
        JcIA()
#appeler la fonction regles_morpon()
regle_morpion()
