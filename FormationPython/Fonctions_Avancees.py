#Différence entre break et return
""""
1- break arrete l'execution d'un boucle et le programme passe à l'instruction qui suit le boucle
   return va arreter l'execution total du programme

2- break peut etre appelé n'importe dans le programme pour interrompre une fil d'exécution
   return ne peut appelé que dans une fonction

3- break ne revoit aucune valeur
   return revoit une valeur de retour

"""

#Fonction Python - Notions Avancées

#CALLBACK



"""def ma_fonction():
    print("toto")
    return 1

a = 5
b = ma_fonction()
print("a", a, "b", b)

a = 5
b = ma_fonction
print("a", a, "b", ma_fonction())"""



def affiche_table(x, op_cbk, result_cbk):
    for i in range(0, 11):
        print(i, op_cbk, x, "=", result_cbk(i, x))

"""def multi_callback(a, b):
    return a*b

def add_callback(a, b):
    return a+b

affiche_table(2, '+', add_callback)"""

#LAMBDA
"""En Python, la fonction anonyme signifie qu’une fonction est sans nom.
Comme nous le savons déjà, le mot-clé def est utilisé pour définir les 
fonctions normales et le mot-clé lambda est utilisé pour créer des fonctions anonymes.
Il a la syntaxe suivante :

Syntaxe:

lambda arguments : expression       """

string ='GeeksforGeeks'
print(lambda string : string) # le lambda n’est pas appelé par la fonction d’impression, 
                              # mais renvoie simplement l’objet de fonction et l’emplacement de mémoire où il est stocké.


"""affiche_table(2, "*", lambda a, b : a*b)
print()
affiche_table(5, "+", lambda a, b : a+b)
print()"""


#Fonction avec nombre variable de parametre

"""def somme(*args):
    resultat = 0
    for i in args:
        resultat += i
    return resultat

print(somme(2, 5, 4))
print()"""

#parametre **args est une parametre cle+valeur

"""def multi(titre, **nombre):
    print("Titre : "+titre)
    resulte = 0
    for i in nombre.values():
        resulte += i
    return resulte

print(multi("Mes multiplication", une=1, deux=2, trois=3))"""




print((lambda a, b : a + b)(5, 6))
