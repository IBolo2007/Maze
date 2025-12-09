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
                        




import random
import networkx as nx


def creer_labyrinthe(largeur, hauteur, diff):
    """create a maze
    """
    laby = nx.Graph()
    arete = list()
    
    for y in range(hauteur):
        for x in range(largeur):
            node = y * largeur + x
            laby.add_node(node, visited=False)
        print (laby.nodes)

    directions = {
        "N": (0, -1),
        "S": (0, 1),
        "E": (1, 0),
        "W": (-1, 0)
    }

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

laby = creer_labyrinthe(4, 3, 30)
            
        
        
        
creer_labyrinthe(4, 3, 30)

    
    
    
    
"""if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)

    print(m)"""
