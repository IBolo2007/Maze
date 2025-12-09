#importation des bibliothèques
import random 
import networkx as nx


def creer_labyrinthe(largeur, hauteur, diff):
    """Créer un labyrinthe parfait fonctionnel.
    """
    laby = nx.Graph()
    arete  = list()
    #been_there = []
    for i in range(largeur):
        for j in range(hauteur):
            laby.add_node(j * largeur + i)
    print(laby.nodes)
    depart = random.choice(laby.nodes)
    if depart:
        been_there.append(depart)
        if been_there == False:
            for voisin in i, j:
                if voisin > j+1 or voisin < j or voisin > i+1 or voisin < i:
                    return None
                else: 
                    s = j+1
                    n = j-1
                    e = i+1
                    w = i-1
                    voisins = [n, e, w, s]
                    for possible in range(voisins.random):
                        depart = possible
        else:
            return None
                        
                    
            
        
        
        
creer_labyrinthe(4, 3, 30)

    
    
    
    
"""if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)
    print(m)"""