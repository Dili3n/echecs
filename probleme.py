from time import sleep
from fltk import *

taille_case = 60

def probleme_win():

    image(240,240,'assets/end.png')
    texte(150,240,"BRAVO !",taille=48)
    mise_a_jour()
    sleep(1)
    return False

def probleme_loose():
    texte(150,240,"PERDU !",taille=48)
    mise_a_jour()
    sleep(0.5)

def affichage_prog_1():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_1[i][0]* taille_case,probleme_1[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_1[7][0]* taille_case,probleme_1[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_1[23][0]* taille_case,probleme_1[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_1[6][0]* taille_case,probleme_1[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_1[22][0]* taille_case,probleme_1[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(50,520,"Echecs et Mats en 1 coup")
    texte(170,560,"Pour les blancs",taille=12)


def affichage_prog_2():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_2[i][0]* taille_case,probleme_2[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_2[7][0]* taille_case,probleme_2[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_2[23][0]* taille_case,probleme_2[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_2[6][0]* taille_case,probleme_2[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_2[22][0]* taille_case,probleme_2[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(50,520,"Echecs et Mats en 1 coup")
    texte(170,560,"Pour les noirs",taille=12)

def affichage_prog_3():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_3[i][0]* taille_case,probleme_3[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_3[7][0]* taille_case,probleme_2[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_3[23][0]* taille_case,probleme_2[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_3[6][0]* taille_case,probleme_3[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_3[22][0]* taille_case,probleme_3[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(75,520,"Avantage en 1 coup")
    texte(170,560,"Pour les blancs",taille=12)

def affichage_prog_4():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_4[i][0]* taille_case,probleme_4[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_4[7][0]* taille_case,probleme_4[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_4[23][0]* taille_case,probleme_4[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_4[6][0]* taille_case,probleme_4[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_4[22][0]* taille_case,probleme_4[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(50,520,"Echecs et Mats en 1 coup")
    texte(170,560,"Pour les blancs",taille=12)
    
def affichage_prog_5():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_5[i][0]* taille_case,probleme_5[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_5[7][0]* taille_case,probleme_5[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_5[23][0]* taille_case,probleme_5[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_5[6][0]* taille_case,probleme_5[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_5[22][0]* taille_case,probleme_5[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(50,520,"Echecs et Mats en 1 coup")
    texte(170,560,"Pour les blancs",taille=12)

def affichage_prog_6():
    """
    Fonction pour afficher l'échiquier et épurer le code.
    """

    image(240,240,'assets/bgechequier.png', tag = 'echiquier')

    for i in range(0,22):
        if 0 <= i < 2:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/tour_blanc.png', ancrage = 'se', tag = 'echiquier' )
            
        elif 2 <= i < 4:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/cavalier_blanc.png', ancrage = 'se', tag = 'echiquier')
              
        elif 4 <= i < 6:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/fou_blanc.png', ancrage = 'se', tag = 'echiquier')     
            
            
        elif 16 <= i < 18:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/tour_noire.png', ancrage = 'se', tag = 'echiquier') 
            
        elif 18 <= i < 20:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/cavalier_noir.png', ancrage = 'se', tag = 'echiquier' )
        elif 20 <= i < 22:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/fou_noir.png', ancrage = 'se', tag = 'echiquier')   
    
    for i in range(8,32):
        if 8 <= i < 16:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/pion_blanc.png', ancrage = 'se', tag = 'echiquier')
        elif 24 <= i < 32:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
              'assets/pion_noir.png', ancrage = 'se', tag = 'echiquier')
            
    for i in range(32,48):
        if 32 <= i < 40:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier')
        if 40 <= i < 48:
            image(probleme_6[i][0]* taille_case,probleme_6[i][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier')
        
    image(probleme_6[7][0]* taille_case,probleme_6[7][1]* taille_case,
          'assets/roi_blanc.png', ancrage = 'se', tag = 'echiquier')
    image(probleme_6[23][0]* taille_case,probleme_6[23][1]* taille_case,
          'assets/roi_noir.png', ancrage = 'se', tag = 'echiquier')
            
    image(probleme_6[6][0]* taille_case,probleme_6[6][1]* taille_case,
          'assets/dame_blanc.png', ancrage = 'se', tag = 'echiquier' )
    image(probleme_6[22][0]* taille_case,probleme_6[22][1]* taille_case,
          'assets/dame_noire.png', ancrage = 'se', tag = 'echiquier' )
    texte(50,520,"Echecs et Mats en 1 coup")
    texte(170,560,"Pour les blancs",taille=12)

probleme_1 = [[4, 8],[8, 8],[7, 6],[-10, -10],[-10, -10],[-10, -10],
              [3, 7],[3, 8], [1, 7],[2, 7],[4, 5],[6, 7],
              [7, 5],[-10, -10],[-10, -10],[-10, -10],[-10, -10],[6, 1],
              [-10, -10],[4, 3],[-10, -10],[1, 4],[5, 2],[7, 1],[1, 2],
              [-10, -10],[3, 3],[4, 4],[2, 3],[6, 2],[7, 2],[8, 2],
              [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[-10,-10],[-10,-10],[-10,-10]]

probleme_2 = [[1, 8],[8, 8],[2, 8],[7, 8],[3, 8],[6, 8], [4, 8],
            [5, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 7],[6, 5],
            [7, 5],[8, 7],[1, 1],[8, 1],[2, 1],[7, 1],[3, 1],
            [6, 1],[4, 1],[5, 1],[1, 2],[2, 2],[3, 2],[4, 2],
            [5, 4],[6, 2],[7, 2],[8, 2],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10]]

probleme_3 = [[1, 8],[8, 8],[4, 4],[6, 6], [3, 5],[3, 8],[4, 8],
          [5, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 5],[6, 7],
          [7, 7],[8, 7],[1, 1],[6, 1],[1, 3],[7, 5],[3, 1],
          [4, 3],[5, 1],[7, 1],[1, 2],[2, 2],[3, 2],[4, 2],
          [5, 4],[6, 3],[7, 2],[8, 2],[-10,-10],[-10,-10],[-10,-10],
          [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
          [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]] 


probleme_4 = [[1, 8],[8, 8],[2, 8],[7, 8],[3, 8],[3, 5], [6, 6], 
          [5, 8],[1, 7],[2, 7],[3, 7],[4, 7],[5, 5],[6, 7],
          [7, 7],[8, 7],[1, 1],[8, 1],[3, 3],[7, 1], [3, 1],
          [3, 4],[4, 1],[5, 1],[1, 2],[2, 2],[3, 2],[4, 2],
          [5, 4],[6, 2],[7, 2],[8, 2], [-10,-10],[-10,-10],[-10,-10],
          [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
          [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]] 

probleme_5 = [[7, 5],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [5,3],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[5,1],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
            [-10,-10],[-10,-10],[-10,-10],[-10,-10]]

probleme_6 = [[1, 7],[-10,-10],[4, 4],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [3, 2],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [7, 6],[8, 5],[5, 1],[-10,-10],[5, 4],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[1, 1],[1, 2],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[7, 2],[8, 3],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10],
              [-10,-10],[-10,-10],[-10,-10],[-10,-10],[-10,-10]]