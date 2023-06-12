# POO

# Classes
    # Une classe est un prototype défini par l’utilisateur à partir duquel des objets sont créés.
    # Les classes fournissent un moyen de regrouper les données et les fonctionnalités.
    # La création d’une nouvelle classe crée un nouveau type d’objet, ce qui permet de créer de nouvelles instances de ce type.
    # Chaque instance de classe peut être associée à des attributs pour maintenir son état.
    # Les instances de classe peuvent également avoir des méthodes (définies par leur classe) pour modifier leur état.

# objets
    # Un objet est une instance d’une classe.
    # Un objet se compose de :
    #   - État: Il est représenté par les attributs d’un objet. Il reflète également les propriétés d’un objet.
    #   - Comportement: Il est représenté par les méthodes d’un objet. Il reflète également la réponse d’un objet à d’autres objets.
    #   - Identité: Il donne un nom unique à un objet et permet à un objet d’interagir avec d’autres objets.
    
# Déclaration d'objects (également appelée instanciation d’une classe)    
    # Lorsqu’un objet d’une classe est créé, la classe est dite instanciée.
    # Toutes les instances partagent les attributs et le comportement de la classe.
    # Mais les valeurs de ces attributs, c’est-à-dire l’état, sont uniques pour chaque objet.
    # Une seule classe peut avoir un nombre quelconque d’instances.


# Le self
    # - Les méthodes de classe doivent avoir un premier paramètre supplémentaire dans la définition de la méthode.
    #   Nous ne donnons pas de valeur pour ce paramètre lorsque nous appelons la méthode, Python le fournit.
    # - 



class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom    # variable d'instance
        self.nom = nom          # variable d'instance

    def mes_infos(self):        # méthode d'instance
        print(f"Je m'appelle {self.prenom} {self.nom}")

    def other():                # méthode de classe
        print("Autre méthode")
personne1 = Personne("Mouhamed", "Sylla")
personne1.mes_infos()
#Personne.mes_infos(personne1)