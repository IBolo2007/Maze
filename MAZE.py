#importation des bibliothèques
import random 
import networkx as nx


def creer_labyrinthe(largeur, hauteur, diff):
    """Créer un labyrinthe parfait fonctionnel.
    """

    laby = nx.Graph()
    #arete  = list()
    been_there = []
    for i in range(largeur):
        for j in range(hauteur):
            laby.add_node(j * largeur + i)
    print("Nœuds créés :", list(laby.nodes))
    depart = random.choice(list(laby.nodes))
    been_there.append(depart)
    
    x = depart % largeur
    y = depart // largeur
    
    while len(been_there) < largeur * hauteur:
        voisins = []
        if y > 0:
            voisins.append(((x, y-1), (y-1) * largeur + x))
        if y < hauteur - 1:
            voisins.append(((x, y+1), (y+1) * largeur + x))
        if y > 0:
            voisins.append(((x+1, y), y * largeur + (x+1)))
        if x < largeur - 1:
            voisins.append(((x+1, y), y * largeur + (x+1)))
        voisins = [v for v in voisins if v[1] not in been_there]
        
        if voisins:
            (xn, yn), new_id = random.choice(voisins)
            laby.add_edge(depart, new_id)
            been_there.append(new_id)
            x, y = xn, yn
            depart = new_id
        else:
            depart = been_there[-2]
            been_there.pop()
            x = depart % largeur
            y = depart // largeur

        (x1, y1), new_id = random.choice(voisins)
        laby.add_edge(depart, new_id)
        been_there.append(new_id)
        x, y = x1, y1
        depart = new_id
    return laby
                        


CODE, KAMRAD

import random
import networkx as nx
import matplotlib.pyplot as plt

def creer_labyrinthe(largeur, hauteur, diff):
    """create a maze
    """
    laby = nx.Graph()
    arete = list()
    
    for y in range(hauteur):
        for x in range(largeur):
            node = y * largeur + x
            laby.add_node(node, visited=False)

    stack = [(0, 0)]
    start_node = 0
    laby.nodes[start_node]["visited"] = True

    while stack:
        x, y = stack[-1]
        node = y * largeur + x


        neighbors = []
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni = x + dx
            nj = y + dy
            if 0 <= ni < largeur and 0 <= nj < hauteur:
                neighbor = nj * largeur + ni
                if not laby.nodes[neighbor]["visited"]:
                    neighbors.append((ni, nj))

        if neighbors:
            ni, nj = random.choice(neighbors)
            new_node = nj * largeur + ni
            laby.add_edge(node, new_node)
            laby.nodes[new_node]["visited"] = True
            stack.append((ni, nj))
        else:
            stack.pop()
    return laby

if __name__ == "__main__":
    largeur =  8
    hauteur = 7    
    laby = creer_labyrinthe(largeur, hauteur, 30)
    pos = {node: (node % largeur, -(node // largeur)) for node in laby.nodes()}
    nx.draw(laby, pos, with_labels=True, node_size=600, node_color='lightblue')
    plt.show()


    
    
    
    
"""if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)

    print(m)"""

"""ancien code :
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
            return None"""

