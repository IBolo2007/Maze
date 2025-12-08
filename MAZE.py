#importation des bibliothèques
import random 
import networkx as nx


def creer_labyrinthe(largeur, hauteur, diff):
    """Créer un labyrinthe parfait fonctionnel.
    """
    laby = nx.Graph()
    arete  = list()
    for i in range(largeur):
        for j in range(hauteur):
            laby.add_node(j * largeur + i)
    print(laby.nodes)
    depart = random.choice(laby.nodes)
    
        
creer_labyrinthe(4, 3, 30)
    
    
if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)
    print(m)