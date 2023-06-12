nom_personne = []
nom = " "
while nom != "":
    
    nom = input("Entrer votre nom : ")
    nom_personne.append(nom)
print()
for i in nom_personne:
    if i != "":
        print("Nom : "+i)
print(len(nom_personne))
    # OU
    # Celui ci évite d'ajouter a notre liste un élément vide

"""nom_personne = []
while True:
    nom = input("Entrer votre nom : ")
    if nom != "":
        nom_personne.append(nom)
    else:
        break

print()

for i in nom_personne:
    if i != "":
        print("Nom : "+i)

print(len(nom_personne))"""
