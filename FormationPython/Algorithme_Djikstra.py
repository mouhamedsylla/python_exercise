graphe = {
    'A': { 'B': 2, 'C': 1  },
    'B': { 'A': 2, 'C': 2, 'D': 1, 'E': 3},
    'C': { 'A': 1, 'B': 2, 'D': 4, 'E': 3, 'F': 5},
    'D': { 'B': 1, 'C': 4, 'E': 3, 'F': 6, 'G': 5},
    'E': { 'B': 3, 'C': 3, 'D': 3, 'F': 1},
    'F': { 'C': 5, 'D': 6, 'E': 1, 'G': 2},
    'G': { 'D': 5, 'F': 2 }    
}


def adjacent(start):
    if start not in graphe:
        return {}
    return graphe[start]

def nearest_point(dictionnary):
    next = min(dictionnary, key=dictionnary.get)
    return next, dictionnary[next]


proche = adjacent('C')
print(nearest_point(proche))
