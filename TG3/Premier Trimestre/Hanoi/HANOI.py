def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return pile == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()

def sommet(pile):
    '''Renvoie la valeur au sommet de la pile sans la supprimer'''
    if est_vide(pile): # on verifie ici si la pile est vide en utilisant est_vide 
        raise IndexError('Pile vide') # affiche un message d'erreur Pile vide
        
    val = depiler(pile) # depile l'element au sommet de la pile
    empiler(pile, val) # on rempile tout de suite pour conserver la pile 
    return val # return la valeur 

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    assert n>=1, "n doit etre superieur ou égal a 1"
    # for i in range(n, 1, -1):
    for i in range(n, 0, -1):
        empiler(pile, i)
        
def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = creer_pile()
    p1 = creer_pile()
    p2 = creer_pile()
    mettre_disques(p0, n)
    return [p0, p1, p2]        