# Collections: Tableaux : Array, Tuples, Listes...
# Tuple() : immutable => Non modifiable
# Liste[] : mutable => Modifiable : rajouter/supprimer des éléments ou les modifier


""""-------------------------LES TUPLES------------------------"""


#ma_tuple = ("Mouhamed", "Abdou", "Moussa", "Issa", "Awa")

#for i in ma_tuple:
 #   print(i)                    # Affiche les éléments du tuple
  #  print(len(i))               #Affiche le nombre de caractère de chaque élément du tuple
   # print(i[1])                 # Affiche le premier caractère de chaque élément 
#print(len(ma_tuple))           # Affiche le nombre d'élément du tableau


"""--------------------------LES LISTES--------------------------"""

ma_liste = ["Rokhaya", "Maguette", "Awa", "Adama"]

#ma_liste.append("Sokhna")   # Ajouter un élément au liste

#del ma_liste[2]             # Supprimer un élément du liste

#def lire_list(a):
#    for i in a:
#        print(i)

#lire_list(ma_liste)

#liste_ajoute = ["Issa", "Moussa", "Mouhamed"]

# pour l'ajout on deux méthodes
    # On boucle
"""for i in liste_ajoute:
    ma_liste.append(i)

for e in ma_liste:
    print(e)"""

    # On utilise exend
"""ma_liste.extend(liste_ajoute)
print(ma_liste)"""

    # On utilise +=
"""ma_liste += liste_ajoute
print(ma_liste)"""

# Insert pour insérer un élément
"""ma_liste.insert(0, "Ahmed")
print(ma_liste)"""

# Trier une liste par ordre alphabétique
"""
#ma_liste.sort() # sort() effectue une opération inplace, le contenu de ma_liste est changé maintenant
#print(ma_liste)

    # On peut trier ma_liste sans changer l'ordre préétabli avec sorted
#liste_trié = sorted(ma_liste) 

#print(ma_liste)
#print(liste_trié)

    # Trier en partant de la sens inverse
#ma_liste.sort(reverse=True)
#print(ma_liste)

#liste_trié = sorted(ma_liste, reverse=True)
#print(liste_trié)"""

# Trier en terme du nombre de caractère
"""ma_liste.sort(key=lambda nom : len(nom), reverse=True)
print(ma_liste)""" 

# min & max
"""mes_number = [30, 15, 20, 5, 1]

print(min(mes_number))
print(max(mes_number))"""

# in, sum
"""
    # in pour savoir si un element est à l'intérieur d'une collection
if "Awa" in ma_liste:
    print("Présent")
else:
    print("Absent")

    # sum pour faire la somme 
print(sum(mes_number))"""

# Swapper deux éléments (échanger)
"""# Nous allons swapper les éléments de ma_liste d'indice 0 et 3
ma_liste[0], ma_liste[3] = ma_liste [3], ma_liste[0]
print(ma_liste)"""

# Join, Split
    # join = Rejoindre -> coller
noms_joint = "-".join(ma_liste)
noms_joint1 = ", ".join(ma_liste)
noms_joint2 = " ".join(ma_liste)
print(noms_joint, "\n", noms_joint1, "\n", noms_joint2)
    # split = Séparer

"""--------------------FONCTIONS ET TUPLES---------------------"""


#def retour_tuple():
#    return "Mouhamed", "Abdou", "Moussa", "Issa", "Awa"

#infos = retour_tuple()
#print(f"Les noms : {infos[0]}, {infos[1]}, {infos[2]}, {infos[3]}, {infos[4]}")


#nom1, nom2, nom3, nom4, nom5 = retour_tuple()
#print(f"Les noms : {nom1}, {nom2}, {nom3}, {nom4}, {nom5}")

#for i in retour_tuple():
#    print(i)

#print()

"""  *************************  """
#ma_tuple = ("Mouhamed", 23, 1.85)

#def mes_infos():
#    return ma_tuple 
#
#
#def donner_informations(nom, age, taille):
#    print(f"Informations: Nom:{nom} Age:{age} Taille:{taille}")

#infos = mes_infos()
#donner_informations(*infos)

#print()

#print(infos)
#print(*infos)  #unpack tuple


"""-----------------------LES SLICES--------------------------

ma_tuple = ("Mouhamed", "Abdou", "Moussa", "Issa", "Awa")

for i in ma_tuple[0:3:2]:  #  [start:stop:step]                   # [:] => Affiche tout les éléments de meme que [::1]
    print(i)                                                      # step specifie le nombre de saut
                                                                  # [::-1] => Affiche tout mais dans le sens opposé

me = ma_tuple # Par la suite tout changement effectuer sur me en est de meme sur ma_tuple et vis versa

me1 = ma_tuple[:] # Ici ma_tuple = me1 mais les changement effectuer sur l'un des deux n'impacte pas l'autre
"""
                                                                  