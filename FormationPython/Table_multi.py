


def afficher_table_multiplication(n, min=1, max=10):
   
    print("TABLE DE "+str(n))

    for i in range(min, int(max+1)):
        result = n*i
        print(f" {n} x {i} = {result} ")

def demande():
    condition = False
    while condition == False:
        nb = input("Quel est table de multiplication voulez-vous afficher : ") # le type de nb donné sera str il faut donc convertir en int
        print()
        print("Définir les valeurs minimale et maximale de votre table de multiplication\n")
        mini = input("Valeur minimale : ")                                     # le type de mini donné sera str il faut donc convertir en int
        maxi = input("Valeur maximale : ")                                     # le type de maxi donné sera str il faut donc convertir ent int
        try:
            n = int(nb)
            max = int(maxi)
            min = int(mini)
            condition = True
        except:
            print("ERREUR! Vous devez entrer des nombres entiers\n")
            print("Réessayer vos entrez")
        else:
            if min > max:
                print("ERREUR! Vous devez entrez un nombre minimale inférieur au nombre maximale")
                condition = False

    afficher_table_multiplication(n, min, max)

demande()
    


