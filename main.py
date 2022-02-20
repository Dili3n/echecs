from fltk import *
import pickle
import os.path
import time
import datetime
from probleme import *
from random import randint

# ========================================================================== #
#                              Les Variables                                 #
# ========================================================================== #


# variables pour le temps (chronomètre, heure)
myDate = datetime.date.fromtimestamp(time.time())
myDateTime = datetime.datetime.fromtimestamp(time.time())
            
# dimensions du jeu
taille_case = 60
largeur_plateau = 10 # en nombre de cases
hauteur_plateau = 10 # en nombre de cases

# Création fenêtre de jeu. 
    
cree_fenetre(taille_case * largeur_plateau,
             taille_case * hauteur_plateau)

# Coordonnées des pièces de l'échiquier.

pieces = [[1, 8],[8, 8], # Tours blancs 0 à 1.
          [2, 8],[7, 8], # Cavaliers blancs 2 à 3.
          [3, 8],[6, 8], # Fous blancs 4 à 5.
          [4, 8], # Dame blanc 6.
          [5, 8], # Roi blanc 7.
          [1, 7],[2, 7],[3, 7],[4, 7],
          [5, 7],[6, 7],[7, 7],[8, 7], # Pions blancs 8 à 15.

          [1, 1],[8, 1], # Tours noirs 16 à 17.
          [2, 1],[7, 1], # Cavaliers noirs 18 à 19.
          [3, 1],[6, 1], # Fous noirs 20 à 21.
          [4, 1], # Dame noir 22.
          [5, 1], # Roi noir 23.
          [1, 2],[2, 2],[3, 2],[4, 2],
          [5, 2],[6, 2],[7, 2],[8, 2], # Pions noirs 24 à 31

          [-10,-10],[-10,-10],[-10,-10],[-10,-10],# 
          [-10,-10],[-10,-10],[-10,-10],[-10,-10],# Dames de 32 à 39 dame blanche
          [-10,-10],[-10,-10],[-10,-10],[-10,-10], #
          [-10,-10],[-10,-10],[-10,-10],[-10,-10]] # Dames de 40 à 47 dame noire

case_x = {1 : "a",2 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h"}
case_y = {1 : 8,2 : 7, 3 : 6, 4 : 5, 5 : 4, 6 : 3, 7 : 2, 8 : 1}

# Savoir à qui c'est le tour.
tour_b = True

# Pour gérer les promotions des blancs et noirs.
promotion_b = 0
promotion_n = 0

# Boucle principale qui fait fonctionner le jeu.
menu = True
boucle = False
pause = False
problemes = False

jeu = True

match_nul = False
 
# Charger une partie
charger = False

# Nom des joueurs
noir = "noir"
blanc = "blanc"

# Rock possible ou non
rock_b = True
rock_n = True

# Diagonale des pions.
pion_diago = [False,False]

histo = open("historique_partie.txt", "w")
histo.write("Historique de la dernière partie :\nBlancs\tNoirs\n")
histo.close()

# varible pour savoir quand la partie a été créé 
creer = ("Créé",myDateTime.day,"/",myDateTime.month,"/",myDateTime.year,"|",myDateTime.hour,":",myDateTime.minute) 

# ========================================================================== #
#                              Les Fonctions                                 #
# ========================================================================== #


def tt_pieces():

    return [[1, 8],[8, 8],[2, 8],[7, 8],[3, 8],[6, 8], [4, 8],
            [5, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 7],
            [7, 7],[8, 7],[1, 1],[8, 1],[2, 1],[7, 1],[3, 1],
            [6, 1],[4, 1],[5, 1],[1, 2],[2, 2],[3, 2],[4, 2],
            [5, 2],[6, 2],[7, 2],[8, 2],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10]]

def piece(x, y):

    """
    Fonction qui transforme les pixels en cases, pour convertir un clic
    effectué sur une des cases de l'echiquier'

    >>> piece(400,300)
    [7,6]

    >>> piece(540,359)
    [10,6]
    """

    x = (x // 60) + 1
    y = (y // 60) + 1
    
    case = [x, y]
    print(case)
    
    return case
        

def change_tour(tour_b, changement_tour):

    """
    Fonction utilisée pour changer de tour. Quand le tour des blancs est fini..
    Paff c'est le tour aux noirs.

    >>> change_tour(True)
    False
    """
    if tour_b == True and changement_tour:   
        tour_b = False
    elif tour_b == False and changement_tour:
        tour_b = True

    return tour_b

def sauvegarde(pieces,tour_b,blanc,noir,creer):

    """
    Fontion utilisée pour sauvegarder une partie en cours.
    La sauvegarde comprend, qui été en train de jouer,
    le nom des joueurs, la date de création de la partie,
    l'échiquier ainsi que l'emplacement des pièces.
    La fonction ouvre un fichier txt pour ensuite y écrire les
    informations.
    """

    save = [pieces, tour_b,blanc,noir,creer] 
    fichier = open("save.txt", "wb")
    pickle.dump(save,fichier)
    fichier.close()

def recuperation():

    """
    Fonction utilisée pour récupérer une sauvegarde dans le fichier
    save.txt
    """

    fichier = open("save.txt", "rb")
    save = pickle.load(fichier)
    fichier.close()
    return save



                #=========================================#
                #             Fonctions PIONS             #
                #=========================================#

def manger_pion(couleur):

    """
    fonction permettant de bouger un pion en diagonal.
    Quand il mange une autre pièce.
    """
    

    if couleur == 1:
        m_1 = [case[0]+1,case[1]-1]
        m_2 = [case[0]-1,case[1]-1]
        
        if m_1 in pieces[16:31] or m_1 in pieces[40:47]:
            pion_diago[0] = True
        elif m_2 in pieces[16:31] or m_2 in pieces[40:47]:
            pion_diago[1] = True
    
    else:
        
        m_1 = [case[0]-1,case[1]+1]
        m_2 = [case[0]+1,case[1]+1]
        
        if m_1 in pieces[0:15] or m_1 in pieces[32:39]:
            pion_diago[0] = True
        if m_2 in pieces[0:15] or m_2 in pieces[32:39]:
            pion_diago[1] = True
            
    return pion_diago


def promotion(cases,promotion,pieces):

    """
    Fonction utilisée pour gérer les promotions. 
    Transforme un pion en dame, quand celui-ci atteind la case voulu.
    Pour les blancs, le pion se transforme une fois la case 1 atteind.
    Pour les noirs, cela sera la case 8
    """
    
    if pieces[pieces.index(cases)][1] == 1:
        promotion += 1
        pieces[pieces.index(cases)] = [-10,-10]
        pieces[31+promotion] = cases
        return promotion
        
    else:
        promotion += 1
        pieces[pieces.index(cases)] = [-10,-10]
        pieces[39+promotion] = cases
        return promotion

                #=========================================#
                #             Fonctions TOURS             #
                #=========================================#

def avancer_tour(case_t,case):

    """
    Fonction utilisée pour faire avancer la tour, (la possibilité de tous
    ses déplacements en ligne)

    >>> avancer_tour([5,3],[5,5])
    True

    """

    for i in range(-10,10):
        if case_t[0] + i == case[0] and case_t[1] == case[1]:
           return True
        elif case_t[0] == case[0] and case_t[1] - i == case[1]:
            return True
        elif case_t[0] - i == case[0] and case_t[1] == case[1]:
            return True
        elif case_t[0] == case[0] and case_t[1] + i == case[1]:
            return True

                #=========================================#
                #             Fonctions FOUS              #
                #=========================================#

def avancer_fou(case_f,case):

    """
    Fonction utilisée pour faire avancer le fou,
    (possiblité de faire les déplacements en diagonale)

    >>> avancer_fou([4,3],[5,4])
    True

    """

    for i in range(-10,10):
        if case_f[0] + i == case[0] and case_f[1] + i == case[1]:
            return True
        if case_f[0] + i == case[0] and case_f[1] - i == case[1]:
            return True
        if case_f[0] - i == case[0] and case_f[1] + i == case[1]:
            return True
        if case_f[0] - i == case[0] and case_f[1] - i == case[1]:
            return True

                #=========================================#
                #             Fonctions CAVALIER          #
                #=========================================#

def avance_cavalier(cases, pieces, couleur):

    """
    Fonction utilisée pour savoir si le cavalier est en possibilité de
    se déplacer en L.
    On regarde si la case visée n'est pas utilisé ou si on y trouve une pièce ennemi,
    dans ce cas la, le cavalier peut avancer.

    """

    if cases not in pieces:
        pieces[pieces.index(case)] = cases
        return True

    if ((cases in pieces[16:31] or cases in pieces[40:47])
         and couleur == 1):
         pieces[pieces.index(cases)] = [-10,-10]
         pieces[pieces.index(case)] = cases
         return True

    if ((cases in pieces[0:15] or cases in pieces[32:39])
         and couleur == 0):
         pieces[pieces.index(cases)] = [-10,-10]
         pieces[pieces.index(case)] = cases
         return True

    else:
        return False


                #=========================================#
                #             Fonctions DAMES             #
                #=========================================#

def avancer_dame(case_d,case):

    """
    Fonction pour faire avancer la dame. Meme fonction que celle du fou et tour.
    Déplacement en diagonale + en ligne

    >>> avancer_dame([5,3],[5,5])
    True

    >>> avancer_dame([4,3],[5,4])
    True

    """

    for i in range(-10,10):
        if case_d[0] + i == case[0] and case_d[1] == case[1]:
            return True
        if case_d[0] == case[0] and case_d[1] - i == case[1]:
            return True
        if case_d[0] - i == case[0] and case_d[1] == case[1]:
            return True
        if case_d[0] == case[0] and case_d[1] + i == case[1]:
            return True
        if case_d[0] + i == case[0] and case_d[1] + i == case[1]:
            return True
        if case_d[0] + i == case[0] and case_d[1] - i == case[1]:
            return True
        if case_d[0] - i == case[0] and case_d[1] + i == case[1]:
            return True              
        if case_d[0] - i == case[0] and case_d[1] - i == case[1]:
            return True

                #=========================================#
                #             Fonctions ROI               #
                #=========================================#

                #=========================================#
                #           Fonctions Affichage           #
                #=========================================#

def touche_piece(case,taille_case):

    """
    En cliquant sur n'importe quelle pièce cette fonction s'activera
    et laissera apparaitre un rectangle rouge autour de la pièce
    selectionnée.
    """
    
    rectangle((case[0]*taille_case)-taille_case,
                          (case[1]*taille_case)-taille_case,
                          case[0]*taille_case,
                          case[1]*taille_case, couleur = 'darkred', epaisseur = '2')

    mise_a_jour()
    attend_clic_gauche()

def affichage():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(pieces[i][0]* taille_case,pieces[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(pieces[7][0]* taille_case,pieces[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(pieces[23][0]* taille_case,pieces[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(pieces[6][0]* taille_case,pieces[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(pieces[22][0]* taille_case,pieces[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )


# ========================================================================== #
#                            Programme Principal                             #
# ========================================================================== #
                        

while jeu:

    while menu:
           image(240,240,'assets/bgmenu.png', tag = 'menu' )
           mise_a_jour()

           chance = randint(1,6)
           ev = donne_ev()
           ty = type_ev(ev)    
        
           if ty == 'Quitte':
        
               menu = False
               jeu = False
               break

           if ty == 'ClicGauche':
        
            if 35 <= abscisse(ev) <= 285 and 270 <= ordonnee(ev) <= 365:
                menu = False
                boucle = True
            if 320 <= abscisse(ev) <= 570 and 270 <= ordonnee(ev) <= 365:
                menu = False
                boucle = True
                charger = True
            if 35 <= abscisse(ev) <= 285 and 390 <= ordonnee(ev) <= 485:
                blanc = input("Pseudo du joueur blanc \n")
                noir = input("Pseudo du joueur noir \n")
            if 320 <= abscisse(ev) <= 570 and 390 <= ordonnee(ev) <= 485:
                menu = False
                problemes = True
        

    while boucle:
        # Pour éviter le changement de tour quand on désélectionne un pièce

        if charger == True:
            charger = False
            save = recuperation()
            creer = save[4]
            noir = save[3]
            blanc = save[2]
            tour_b = save[1]
            pieces = save[0]

        prehistorique = 0
        historique = 0

        changement_tour = True

        case0 = 0
        case1 = 0

        avance_fou = False
        avance_dame = False
        avance_tour = False

        indice = 0

        myDate = datetime.date.fromtimestamp(time.time())
        myDateTime = datetime.datetime.fromtimestamp(time.time())

        heure = (myDateTime.day,"/",myDateTime.month,"/",myDateTime.year,"|",myDateTime.hour,":",myDateTime.minute,":",myDateTime.second) 
                           
                    #=========================================#
                    #           Affichage des pièces          #
                    #=========================================#
     
        efface_tout()

        affichage()
        texte(350,495,creer,taille=6)
        texte(22,495,heure,taille=10)
        texte(500,75,noir, taille=13)
        texte(500,375,blanc, taille=13,couleur='white')

        # Mise à jour graphique.
        mise_a_jour()

        # Création des évenements (quitter et clic gauche)
        ev = donne_ev()
        ty = type_ev(ev)    
        
        if ty == 'Quitte':
        
            boucle = False
            jeu = False
            break
    
        if ty == 'ClicGauche':
        
            # Quand un clic est effectué sur l'ensemble de l'échiquier.
            if 0 <= abscisse(ev) <= taille_case * 10 and 0 <= ordonnee(ev) <= taille_case * 10:
            
                case = piece(abscisse(ev), ordonnee(ev))
            


                    #=========================================#
                    #            Les pions blancs             #
                    #=========================================#

                if case in pieces[8:16] and tour_b:
                
                    print("pion blanc")
                
                    # Fonction pion_diago (quand une pièce se trouve en diagonal)
                    pion_diago = manger_pion(1)
                    
                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)
                
                    if ty == 'ClicGauche':

                        # === Avancé du pion : 1 Case === #

                        if ((case[0]*taille_case)-taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case) and
                            (case[1]*taille_case)-taille_case*2 
                            <= ordonnee_souris() <=
                            (case[1]*taille_case)-taille_case
                            and [case[0],case[1]-1] not in pieces):
                        
                            pieces[pieces.index(case)] = [case[0],case[1]-1]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]]) + str(case_y[case[1]-1])

                        
                            # === PROMOTION D'UN PION === #
                            if pieces[pieces.index([case[0],case[1]-1])][1] == 1:
                                historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]]) + str(case_y[case[1]-1])
                                promotion_b = (promotion([case[0],case[1]-1],     
                                               promotion_b, pieces))
                            mise_a_jour()
                        
                        
                        # === L'engagement du pion : 2 Cases === #
             
                
                        elif (((case[0]*taille_case)-taille_case
                              <= abscisse_souris() <=
                              (case[0]*taille_case) and
                              (case[1]*taille_case)-taille_case*3 
                              <= ordonnee_souris() <=
                              (case[1]*taille_case)-taille_case*2)
                              and case[1] == 7
                              and [case[0],case[1]-2] not in pieces):
                        
                            pieces[pieces.index(case)] = [case[0],case[1]-2]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]]) + str(case_y[case[1]-2])
                            mise_a_jour()


                    # === Les pions blancs mangent les noirs === #


                        elif ((case[0]*taille_case)
                              <= abscisse_souris() <=
                              (case[0]*taille_case)+taille_case and 
                              (case[1]*taille_case)-taille_case*2 
                              <= ordonnee_souris() <= 
                              (case[1]*taille_case)-taille_case and
                              pion_diago[0] == True):
                        
                            pieces[pieces.index([case[0]+1,case[1]-1])] = [-10,-10]
                            pieces[pieces.index(case)] = [case[0]+1,case[1]-1]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]-1])
                        
                            if pieces[pieces.index([case[0]+1,case[1]-1])][1] == 1:
                                promotion_b = (promotion([case[0]+1,case[1]-1],
                                               promotion_b, pieces))
                        
                        elif ((case[0]*taille_case)-taille_case*2
                              <= abscisse_souris() <=
                              (case[0]*taille_case)-taille_case and 
                              (case[1]*taille_case)-taille_case*2
                              <= ordonnee_souris() <= 
                              (case[1]*taille_case)-taille_case and pion_diago[1] == True):
                            pieces[pieces.index([case[0]-1,case[1]-1])] = [-10,-10]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]-1])
                            pieces[pieces.index(case)] = [case[0]-1,case[1]-1]
                        
                            # === PROMOTION D'UN PION === #
                            if pieces[pieces.index([case[0]-1,case[1]-1])][1] == 1:
                                promotion_b = (promotion([case[0]-1,case[1]-1],    
                                               promotion_b, pieces))
                            
                            
            # === ELSE : Quand une pièce est deselectionné ou pas touché === #


                        else:
                            changement_tour = False

                        tour_b = change_tour(tour_b, changement_tour)
             
                    #=========================================#
                    #            Les pions noirs              #
                    #=========================================#
                
                elif case in pieces[24:32] and not tour_b:
                    print("pion noir")
            
                    pion_diago = manger_pion(2)

                    touche_piece(case,taille_case)
                    
                    if ty == 'ClicGauche':

                        # === Avancé du pion : 1 Case === #

                        if ((case[0]*taille_case)-taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case) and
                            (case[1]*taille_case) 
                            <= ordonnee_souris() <=
                            (case[1]*taille_case)+taille_case 
                            and [case[0],case[1]+1] not in pieces):

                            pieces[pieces.index(case)] = [case[0],case[1]+1]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]]) + str(case_y[case[1]+1])

                            # === PROMOTION D'UN PION === #
                            if pieces[pieces.index([case[0],case[1]+1])][1] == 8:
                                promotion_n = (promotion([case[0],case[1]+1],
                                               promotion_n,pieces))
                            mise_a_jour()
                        
                            # === L'engagement du pion : 2 Cases === #

                        elif (((case[0]*taille_case)-taille_case
                             <= abscisse_souris() <=
                             (case[0]*taille_case) and
                             (case[1]*taille_case)+ taille_case
                             <= ordonnee_souris() <=
                             (case[1]*taille_case)+ taille_case*2) and case[1] == 2
                            and [case[0],case[1]+2] not in pieces):

                            pieces[pieces.index(case)] = [case[0],case[1]+2]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]]) + str(case_y[case[1]+2])
                            mise_a_jour()
                        
                           # === Les pions noirs mangent les blancs === #

                        elif ((case[0]*taille_case)-taille_case*2
                             <= abscisse_souris() <=
                             (case[0]*taille_case)-taille_case and 
                             (case[1]*taille_case) 
                             <= ordonnee_souris() <= 
                             (case[1]*taille_case)+taille_case and pion_diago[0] == True):

                            pieces[pieces.index([case[0]-1,case[1]+1])] = [-10,-10]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]+1])
                            pieces[pieces.index(case)] = [case[0]-1,case[1]+1]

                            # === PROMOTION D'UN PION === #
                            if pieces[pieces.index([case[0]-1,case[1]+1])][1] == 8:
                                promotion_n = (promotion([case[0]-1,case[1]+1],
                                               promotion_n,pieces))
                        
                        elif ((case[0]*taille_case)
                              <= abscisse_souris() <=
                              (case[0]*taille_case)+taille_case and 
                              (case[1]*taille_case)
                              <= ordonnee_souris() <= 
                              (case[1]*taille_case)+taille_case and pion_diago[1] == True):
                            pieces[pieces.index([case[0]+1,case[1]+1])] = [-10,-10]
                            pieces[pieces.index(case)] = [case[0]+1,case[1]+1]
                            historique = "P" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]+1])


                            # === PROMOTION D'UN PION === #
                            if pieces[pieces.index([case[0]+1,case[1]+1])][1] == 8:
                                promotion_n = (promotion([case[0]+1,case[1]+1],
                                               promotion_n,pieces))
                            
                        else:
                            changement_tour = False
                        
                        tour_b = change_tour(tour_b, changement_tour)
                        
                    #=========================================#
                    #            Les tours blanches           #
                    #=========================================#
                                                                   
                elif (case in pieces[:2]) and tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_t = piece(abscisse_souris(), ordonnee_souris())

                        avance_tour = avancer_tour(case_t,case)

                        while case_t != case and avance_tour:

                            if case_t in pieces:
                                indice += 1
                                if indice == 1 and (case_t in pieces[16:32] or case_t in pieces[40:48]):
                                    avance_tour = True
                                elif indice > 1 or (case_t in pieces[0:16] or case_t in pieces[32:40]):
                                    avance_tour = False
                                elif indice == 0 :
                                    avance_tour = True

                            if case_t[0] < case[0]:
                                case0 -= 1
                                case_t[0] += 1
                            if case_t[0] > case[0]:
                                case0 += 1
                                case_t[0] -= 1
                            if case_t[1] < case[1]:
                                case1 -= 1
                                case_t[1] += 1
                            if case_t[1] > case[1]:
                                case1 += 1
                                case_t[1] -= 1

                        case_t[0] += case0
                        case_t[1] += case1

                        if ((case_t in pieces[16:32] or case_t in pieces[40:48]) and avance_tour
                            and case_t not in pieces[0:2]):
                            pieces[pieces.index(case_t)] = [-10,-10]
                            pieces[pieces.index(case)] = case_t

                        elif avance_tour and case_t not in pieces:
                            pieces[pieces.index(case)] = case_t


                        else:
                            changement_tour = False

                        historique = "T" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_t[0]]) + str(case_y[case_t[1]])
                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #            Les tours noires             #
                    #=========================================#

                elif case in pieces[16:18] and not tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_t = piece(abscisse_souris(), ordonnee_souris()) 

                        avance_tour = avancer_tour(case_t,case)

                        while case_t != case and avance_tour:
                        
                            if case_t in pieces:
                                indice += 1
                                if indice == 1 and (case_t in pieces[0:16] or case_t in pieces[32:40]):
                                    avance_tour = True
                                elif indice > 1 or (case_t in pieces[16:32] or case_t in pieces[40:48]):
                                    avance_tour = False
                                elif indice == 0 :
                                    avance_tour = True

                            if case_t[0] < case[0]:
                                case0 -= 1
                                case_t[0] += 1
                            if case_t[0] > case[0]:
                                case0 += 1
                                case_t[0] -= 1
                            if case_t[1] < case[1]:
                                case1 -= 1
                                case_t[1] += 1
                            if case_t[1] > case[1]:
                                case1 += 1
                                case_t[1] -= 1

                        case_t[0] += case0
                        case_t[1] += case1

                        if ((case_t in pieces[0:16] or case_t in pieces[32:40]) and avance_tour
                             and case_t not in pieces[16:18]):
                            pieces[pieces.index(case_t)] = [-10,-10]
                            pieces[pieces.index(case)] = case_t

                        elif avance_tour and case_t not in pieces:
                            pieces[pieces.index(case)] = case_t


                        else:
                            changement_tour = False

                        historique = "T" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_t[0]]) + str(case_y[case_t[1]])
                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #            Les cavaliers blancs         #
                    #=========================================#

                elif case in pieces[2:4] and tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        if ((case[0]*taille_case)-taille_case*3
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case*2 and
                            case[1]*taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case):

                            cases = [case[0]-2,case[1]+1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-2]) + str(case_y[case[1]+1])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case)+taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case*2 and
                            case[1]*taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case):

                            cases = [case[0]+2,case[1]+1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+2]) + str(case_y[case[1]+1])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case and
                            case[1]*taille_case+taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case*2):

                            cases = [case[0]+1,case[1]+2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]+2])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case-taille_case*2)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case and
                            case[1]*taille_case+taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case*2):

                            cases = [case[0]-1,case[1]+2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]+2])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case)-taille_case*3
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case*2 and
                            case[1]*taille_case-taille_case*2
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case):

                            cases = [case[0]-2,case[1]-1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-2]) + str(case_y[case[1]-1])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case)+taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case*2 and
                            case[1]*taille_case-taille_case*2
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case):

                            cases = [case[0]+2,case[1]-1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+2]) + str(case_y[case[1]-1])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case and
                            case[1]*taille_case-taille_case*3
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case*2):

                            cases = [case[0]+1,case[1]-2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]-2])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        elif ((case[0]*taille_case-taille_case*2)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case and
                            case[1]*taille_case-taille_case*3
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case*2):

                            cases = [case[0]-1,case[1]-2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]-2])
                            changement_tour = avance_cavalier(cases, pieces, 1)

                        else:
                            changement_tour = False
                            
                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #            Les cavaliers noirs          #
                    #=========================================#

                elif case in pieces[18:20] and not tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        if ((case[0]*taille_case)-taille_case*3
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case*2 and
                            case[1]*taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case):

                            cases = [case[0]-2,case[1]+1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-2]) + str(case_y[case[1]+1])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case)+taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case*2 and
                            case[1]*taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case):

                            cases = [case[0]+2,case[1]+1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+2]) + str(case_y[case[1]+1])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case and
                            case[1]*taille_case+taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case*2):

                            cases = [case[0]+1,case[1]+2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]+2])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case-taille_case*2)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case and
                            case[1]*taille_case+taille_case
                            <= ordonnee_souris() <=
                            case[1]*taille_case+taille_case*2):

                            cases = [case[0]-1,case[1]+2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]+2])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case)-taille_case*3
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case*2 and
                            case[1]*taille_case-taille_case*2
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case):

                            cases = [case[0]-2,case[1]-1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-2]) + str(case_y[case[1]-1])
                            changement_tour =  avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case)+taille_case
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case*2 and
                            case[1]*taille_case-taille_case*2
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case):

                            cases = [case[0]+2,case[1]-1]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+2]) + str(case_y[case[1]-1])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)+taille_case and
                            case[1]*taille_case-taille_case*3
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case*2):

                            cases = [case[0]+1,case[1]-2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]+1]) + str(case_y[case[1]-2])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        elif ((case[0]*taille_case-taille_case*2)
                            <= abscisse_souris() <=
                            (case[0]*taille_case)-taille_case and
                            case[1]*taille_case-taille_case*3
                            <= ordonnee_souris() <=
                            case[1]*taille_case-taille_case*2):

                            cases = [case[0]-1,case[1]-2]
                            historique = "C" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case[0]-1]) + str(case_y[case[1]-2])
                            changement_tour = avance_cavalier(cases, pieces, 0)

                        else:
                            changement_tour = False

                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #            Les fous blancs              #
                    #=========================================#

                # jusqu'à 7 pour faire la dame aussi
                elif (case in pieces[4:6]) and tour_b:
                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_f = piece(abscisse_souris(), ordonnee_souris()) 

                        avance_fou = avancer_fou(case_f,case)

                        while case_f != case and avance_fou:

                            if case_f in pieces:
                                indice += 1
                                if indice == 1 and (case_f in pieces[16:32] or case_f in pieces[40:48]):
                                    avance_fou = True
                                elif indice > 1 or (case_f in pieces[0:16] or case_f in pieces[32:40]):
                                    avance_fou = False
                                elif indice == 0 :
                                    avance_fou = True

                            if case_f[0] < case[0] and case_f[1] < case[1]:
                                case0 -= 1
                                case_f[0] += 1
                                case1 -= 1
                                case_f[1] += 1
                            if case_f[0] < case[0] and case_f[1] > case[1]:
                                case0 -= 1
                                case_f[0] += 1
                                case1 += 1
                                case_f[1] -= 1 
                            if case_f[0] > case[0] and case_f[1] < case[1]:
                                case0 += 1
                                case_f[0] -= 1
                                case1 -= 1
                                case_f[1] += 1
                            if case_f[0] > case[0] and case_f[1] > case[1]:
                                case0 += 1
                                case_f[0] -= 1
                                case1 += 1
                                case_f[1] -= 1

                        case_f[0] += case0
                        case_f[1] += case1
                        if ((case_f in pieces[16:32] or case_f in pieces[40:48]) and avance_fou and
                            case_f not in pieces[4:6]):
                            pieces[pieces.index(case_f)] = [-10,-10]
                            pieces[pieces.index(case)] = case_f

                        elif avance_fou and case_f not in pieces:
                            pieces[pieces.index(case)] = case_f


                        else:
                            changement_tour = False

                        historique = "F" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_f[0]]) + str(case_y[case_f[1]])
                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #            Les fous noirs               #
                    #=========================================#

                elif case in pieces[20:22] and not tour_b:
                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_f = piece(abscisse_souris(), ordonnee_souris()) 

                        avance_fou = avancer_fou(case_f,case)

                        while case_f != case and avance_fou:

                            if case_f in pieces:
                                indice += 1
                                if indice == 1 and (case_f in pieces[0:16] or case_f in pieces[32:40]):
                                    avance_fou = True
                                elif indice > 1 or (case_f in pieces[16:32] or case_f in pieces[40:48]):
                                    avance_fou = False
                                elif indice == 0 :
                                    avance_fou = True

                            if case_f[0] < case[0] and case_f[1] < case[1]:
                                case0 -= 1
                                case_f[0] += 1
                                case1 -= 1
                                case_f[1] += 1
                            if case_f[0] < case[0] and case_f[1] > case[1]:
                                case0 -= 1
                                case_f[0] += 1
                                case1 += 1
                                case_f[1] -= 1 
                            if case_f[0] > case[0] and case_f[1] < case[1]:
                                case0 += 1
                                case_f[0] -= 1
                                case1 -= 1
                                case_f[1] += 1
                            if case_f[0] > case[0] and case_f[1] > case[1]:
                                case0 += 1
                                case_f[0] -= 1
                                case1 += 1
                                case_f[1] -= 1

                        case_f[0] += case0
                        case_f[1] += case1

                        if ((case_f in pieces[0:16] or case_f in pieces[32:40]) and avance_fou and
                            case_f not in pieces[20:22]):
                            pieces[pieces.index(case_f)] = [-10,-10]
                            pieces[pieces.index(case)] = case_f

                        elif avance_fou and case_f not in pieces:
                            pieces[pieces.index(case)] = case_f


                        else:
                            changement_tour = False

                        historique = "F" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_f[0]]) + str(case_y[case_f[1]])
                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #               Roi Blanc                 #
                    #=========================================#

                elif case == pieces[7] and tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_r = piece(abscisse_souris(), ordonnee_souris()) 

                        if ((case[0] == case_r[0] and case[1] == case_r[1]+1 or
                            case[0] == case_r[0] and case[1] == case_r[1]-1 or
                            case[0] == case_r[0]+1 and case[1] == case_r[1] or
                            case[0] == case_r[0]-1 and case[1] == case_r[1]+1 or
                            case[0] == case_r[0]-1 and case[1] == case_r[1]-1 or
                            case[0] == case_r[0]+1 and case[1] == case_r[1]+1 or
                            case[0] == case_r[0]-1 and case[1] == case_r[1] or
                            case[0] == case_r[0]+1 and case[1] == case_r[1]-1) and
                            case_r not in pieces[0:16] and case_r not in pieces[32:40]):

                            if ([case_r[0]-1,case_r[1]-1] == pieces[23] or [case_r[0]-1,case_r[1]] == pieces[23] or [case_r[0]-1,case_r[1]+1] == pieces[23] 
                                or [case_r[0]+1,case_r[1]-1] == pieces[23] or [case_r[0]+1,case_r[1]]  == pieces[23] or
                               [case_r[0]+1,case_r[1]+1] == pieces[23] or [case_r[0],case_r[1]-1] == pieces[23] or [case_r[0],case_r[1]+1] == pieces[23]):

                                changement_tour = False

                            if case_r in pieces and changement_tour:
                                pieces[pieces.index(case_r)] = [-10,-10]                            

                            if changement_tour:

                                historique = "R" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_r[0]]) + str(case_y[case_r[1]])
                                pieces[pieces.index(case)] = case_r

                            rock_b = False

                        ### OPTION DU ROCK (petit rock et grand rock)

                        elif ((case[0] == case_r[0]-2 and case[1] == case_r[1]) and
                            [6,8] not in pieces and [7,8] not in pieces and
                            pieces[1] == [8,8]) and rock_b == True:
                            rock_b = False
                            historique = "0-0"
                            pieces[1] = [6,8]
                            pieces[7] = case_r

                        elif ((case[0] == case_r[0]+2 and case[1] == case_r[1]) and
                            [4,8] not in pieces and [3,8] not in pieces and [2,8] not
                            in pieces and pieces[0] == [1,8]) and rock_b == True:
                            rock_b = False
                            historique = "0-0-0"
                            pieces[0] = [4,8]
                            pieces[7] = case_r


                        else:
                            changement_tour = False

                        tour_b = change_tour(tour_b, changement_tour)

                    #=========================================#
                    #                Roi Noir                 #
                    #=========================================#

                elif case == pieces[23] and not tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_r = piece(abscisse_souris(), ordonnee_souris()) 

                        if ((case[0] == case_r[0] and case[1] == case_r[1]+1 or
                            case[0] == case_r[0] and case[1] == case_r[1]-1 or
                            case[0] == case_r[0]+1 and case[1] == case_r[1] or
                            case[0] == case_r[0]-1 and case[1] == case_r[1]+1 or
                            case[0] == case_r[0]-1 and case[1] == case_r[1]-1 or
                            case[0] == case_r[0]+1 and case[1] == case_r[1]+1 or
                            case[0] == case_r[0]-1 and case[1] == case_r[1] or
                            case[0] == case_r[0]+1 and case[1] == case_r[1]-1) and
                            case_r not in pieces[16:32] and case_r not in pieces[40:48]):

                            if ([case_r[0]-1,case_r[1]-1] == pieces[7] or [case_r[0]-1,case_r[1]] == pieces[7] or [case_r[0]-1,case_r[1]+1] == pieces[7] 
                                or [case_r[0]+1,case_r[1]-1] == pieces[7] or [case_r[0]+1,case_r[1]]  == pieces[7] or
                               [case_r[0]+1,case_r[1]+1] == pieces[7] or [case_r[0],case_r[1]-1] == pieces[7] or [case_r[0],case_r[1]+1] == pieces[7]):

                                changement_tour = False
                            
                            if case_r in pieces and changement_tour:
                                pieces[pieces.index(case_r)] = [-10,-10]

                            if changement_tour:

                                historique = "R" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_r[0]]) + str(case_y[case_r[1]])
                                pieces[pieces.index(case)] = case_r

                            rock_n = False

                        ### OPTION DU ROCK (petit rock et grand rock)

                        elif ((case[0] == case_r[0]-2 and case[1] == case_r[1]) and
                            [6,1] not in pieces and [7,1] not in pieces and
                            pieces[17] == [8,1]) and rock_n == True:
                            rock_n = False
                            historique = "0-0"
                            pieces[17] = [6,1]
                            pieces[23] = case_r

                        elif ((case[0] == case_r[0]+2 and case[1] == case_r[1]) and
                            [4,1] not in pieces and [3,1] not in pieces and [2,1] not
                            in pieces and pieces[16] == [1,1]) and rock_n == True:
                            rock_n = False
                            historique = "0-0-0"
                            pieces[16] = [4,1]
                            pieces[23] = case_r

                        else:
                            changement_tour = False

                        tour_b = change_tour(tour_b, changement_tour)



                    #=========================================#
                    #            La Dame blanche              #
                    #=========================================#

                elif (case in pieces[32:40] or case == pieces[6]) and tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_d = piece(abscisse_souris(), ordonnee_souris()) 

                        avance_dame = avancer_dame(case_d,case)

                        while case_d != case and avance_dame:

                            if case_d in pieces:
                                indice += 1
                                print(case_d,case)
                                if indice == 1 and (case_d in pieces[16:32] or case_d in pieces[40:48]):
                                    avance_dame = True
                                elif indice > 1 or (case_d in pieces[0:16] or case_d in pieces[32:40]):
                                    avance_dame = False
                                elif indice == 0 :
                                    avance_dame = True

                            if case[1] == case_d[1] or case[0] == case_d[0]:

                                if case_d[0] < case[0]:
                                    case0 -= 1
                                    case_d[0] += 1
                                if case_d[0] > case[0]:
                                    case0 += 1
                                    case_d[0] -= 1
                                if case_d[1] < case[1]:
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[1] > case[1]:
                                    case1 += 1
                                    case_d[1] -= 1
                            else:

                                if case_d[0] < case[0] and case_d[1] < case[1]:
                                    case0 -= 1
                                    case_d[0] += 1
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[0] < case[0] and case_d[1] > case[1]:
                                    case0 -= 1
                                    case_d[0] += 1
                                    case1 += 1
                                    case_d[1] -= 1 
                                if case_d[0] > case[0] and case_d[1] < case[1]:
                                    case0 += 1
                                    case_d[0] -= 1
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[0] > case[0] and case_d[1] > case[1]:
                                    case0 += 1
                                    case_d[0] -= 1
                                    case1 += 1
                                    case_d[1] -= 1


                        case_d[0] += case0
                        case_d[1] += case1

                        if ((case_d in pieces[16:32] or case_d in pieces[40:48]) and avance_dame == True
                            and case_d != pieces[6]):
                            pieces[pieces.index(case_d)] = [-10,-10]
                            pieces[pieces.index(case)] = case_d

                        elif avance_dame and case_d not in pieces:
                            pieces[pieces.index(case)] = case_d


                        else:
                            changement_tour = False

                        historique = "D" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_d[0]]) + str(case_y[case_d[1]])
                        tour_b = change_tour(tour_b, changement_tour)
                    
                    #=========================================#
                    #             La Dame noire               #
                    #=========================================#

                elif (case == pieces[22] or case in pieces[40:48]) and not tour_b:

                    # Fonction touche_piece (quand on clic sur un piece)
                    touche_piece(case,taille_case)

                    if ty == 'ClicGauche':

                        case_d = piece(abscisse_souris(), ordonnee_souris()) 

                        avance_dame = avancer_dame(case_d,case)

                        while case_d != case and avance_dame:

                            if case_d in pieces:
                                indice += 1
                                print(case_d,case)
                                if indice == 1 and (case_d in pieces[0:16] or case_d in pieces[32:40]):
                                    avance_dame = True
                                elif indice > 1 or (case_d in pieces[16:32] or case_d in pieces[40:48]):
                                    avance_dame = False
                                elif indice == 0 :
                                    avance_dame = True

                            if case[1] == case_d[1] or case[0] == case_d[0]:

                                if case_d[0] < case[0]:
                                    case0 -= 1
                                    case_d[0] += 1
                                if case_d[0] > case[0]:
                                    case0 += 1
                                    case_d[0] -= 1
                                if case_d[1] < case[1]:
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[1] > case[1]:
                                    case1 += 1
                                    case_d[1] -= 1
                            else:

                                if case_d[0] < case[0] and case_d[1] < case[1]:
                                    case0 -= 1
                                    case_d[0] += 1
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[0] < case[0] and case_d[1] > case[1]:
                                    case0 -= 1
                                    case_d[0] += 1
                                    case1 += 1
                                    case_d[1] -= 1 
                                if case_d[0] > case[0] and case_d[1] < case[1]:
                                    case0 += 1
                                    case_d[0] -= 1
                                    case1 -= 1
                                    case_d[1] += 1
                                if case_d[0] > case[0] and case_d[1] > case[1]:
                                    case0 += 1
                                    case_d[0] -= 1
                                    case1 += 1
                                    case_d[1] -= 1



                        case_d[0] += case0
                        case_d[1] += case1

                        if ((case_d in pieces[0:16] or case_d in pieces[32:40]) and avance_dame == True
                            and case_d != pieces[22]):
                            pieces[pieces.index(case_d)] = [-10,-10]
                            pieces[pieces.index(case)] = case_d

                        elif avance_dame and case_d not in pieces:
                            pieces[pieces.index(case)] = case_d


                        else:
                            changement_tour = False

                        historique = "D" + str(case_x[case[0]]) + str(case_y[case [1]]) + " " + str(case_x[case_d[0]]) + str(case_y[case_d[1]])
                        tour_b = change_tour(tour_b, changement_tour)


                elif case == [10,1]:
                    pause = True

            mise_a_jour()

        pion_diago = [False,False]

        if (pieces[0:7] == [[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]] and
            pieces[8:23] == [[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
                             [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]] and
            pieces[24:48] == [[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
                             [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
                             [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]]):
            match_nul = True

        if match_nul:

            image(240,240,'assets/end.png')
            texte(150,240,"Match Nul !",taille=48)
            mise_a_jour()
            sleep(1)
            boucle = False
            menu = True
            match_nul = False


        while pause:
            efface_tout()
            image(240,240,'assets/bgechequierpause.png', tag = 'pause')
            mise_a_jour()

            ev = donne_ev()
            ty = type_ev(ev)    
        
            if ty == 'Quitte':
        
                boucle = False
                pause = False
                jeu = False
                break
    
            if ty == 'ClicGauche':

                if 40 <= abscisse(ev) <= 270 and 198 <= ordonnee(ev) <= 268:

                    pieces = tt_pieces()
                    tour_b = True
                    promotion_b = 0
                    promotion_n = 0
                    pause = False

                if 320 <= abscisse(ev) <= 550 and 198 <= ordonnee(ev) <= 268:

                    sauvegarde(pieces,tour_b,blanc,noir,creer)
                    print("Sauvegardé")

                    rectangle(40,298,270,368)

                if 40 <= abscisse(ev) <= 270 and 298 <= ordonnee(ev) <= 368:

                    pause = False

                if 320 <= abscisse(ev) <= 550 and 298 <= ordonnee(ev) <= 368:

                    pieces = tt_pieces()
                    boucle = False
                    pause = False
                    menu = True

        if historique != prehistorique:
            histo = open("historique_partie.txt", "a")
            if tour_b:
                histo.write(historique + '\n')
            else:
                histo.write(historique + '\t')
            histo.close()
            prehistorique = historique


        mise_a_jour()


    while problemes:

        menu = True 

        efface_tout()

        if chance == 1:
            affichage_prog_1()

        if chance == 2:
            affichage_prog_2()

        if chance == 3:
            affichage_prog_3()

        if chance == 4:
            affichage_prog_4()
            
        if chance == 5:
            affichage_prog_5()

        if chance == 6:
            affichage_prog_6()

        ev = donne_ev()
        ty = type_ev(ev)    
        
        if ty == 'Quitte':
        
            problème = False
            jeu = False
            break

        elif ty == 'ClicGauche':

            case = piece(abscisse(ev), ordonnee(ev))

            if case == [10,1]:
                problemes = False

            elif case == [3,7] and chance == 1:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [8,2]:
                        affichage()
                        problemes = probleme_win()

            elif case == [4,1] and chance == 2:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [8,5]:
                        affichage()
                        problemes = probleme_win()

            elif case == [4,4] and chance == 3:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [3,2]:
                        affichage()
                        problemes = probleme_win()

            elif case == [6,6] and chance == 4:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [6,2]:
                        affichage()
                        problemes = probleme_win()
                        
            elif case == [7,5] and chance == 5:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [7,1]:
                        affichage()
                        problemes = probleme_win()

            elif case == [4,4] and chance == 6:

                if ty == 'ClicGauche':
                    touche_piece(case,taille_case)
                    case_d = piece(abscisse_souris(), ordonnee_souris())
                    if case_d == [2,3]:
                        affichage()
                        problemes = probleme_win()





            else:
                touche_piece(case,taille_case)
                case_d = piece(abscisse_souris(), ordonnee_souris())
                probleme_loose()

            # Mise à jour graphique.

        mise_a_jour()

    

ferme_fenetre()
    
    

    
