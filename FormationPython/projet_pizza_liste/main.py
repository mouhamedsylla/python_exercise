pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]

vide = ()
#def tri_personnalise(e):
#   return len(e)
def affiche(entre, m=-1):
    if entre != ():
        nbpizza = len(pizzas)
        print(f"---- LISTE DES PIZZAS ({nbpizza}) ----")
        entre.sort()
        #entre.sort(reverse=True, key=tri_personnalise)
        c = entre  # On utilise pour définir un slice, m est ici un paramétre optionnel
        if not m == -1:
            c = entre[0:m]
        for i in c:
            print(i)
        print()
        n = int(nbpizza - 1)
        for i in entre[::n]:
            print(i)
    else:
        print("AUCUNE PIZZA")

def ajout_pizza(entre):
    print("Voulez-vous ajouter un pizza ? (Si oui, entré 'o' si non, entré 'n'")
    choix = input("Votre choix o/n: ")

    if choix == 'o':  
        pizza_exist = True
        while pizza_exist == True:
            aj_pizza = input("Pizza à ajouter: ")
            if aj_pizza.lower() in entre:
                print("Ce pizza exite déjà")
                pizza_exist = True
            else:
                entre.append(aj_pizza)
                pizza_exist = False
    elif choix == 'n':
        print("Merci !!")
        return menu(entre)

def menu(entre):
    print(" - - - -  MENU - - - -")
    print("     Choississez un options")
    print("1.Afficher vos pizza")
    print("2.Ajouter un pizza")
    print("3.Quitter le programme")
    option = 0 
    while option != '3':
        option = input("Entré un option : ")
        if option == '1':
            affiche(entre) # Si on ne définit pas le paramètre m, tout les éléments vont etre afficher
        elif option == '2':
            ajout_pizza(entre)
        elif option != '3':
            print("     Choississez un options")
    print("Vous venez de quitter le prgramme.")
    return
menu(pizzas)