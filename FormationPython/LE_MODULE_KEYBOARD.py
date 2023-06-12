#   LE MODULE KEYBOARD
"""
Python fournit une bibliothèque nommée keyboard qui est utilisée pour obtenir le contrôle total du clavier.
C'est une petite bibliothèque Python qui peut accrocher des événements globaux, enregistrer des raccourcis clavier,
simuler des pressions sur les touches et bien plus encore.

    * Il aide à saisir les touches, à enregistrer les activités du clavier et à bloquer les touches 
    jusqu'à ce qu'une touche spécifiée soit saisie et à simuler les touches.
    * Il capture toutes les touches, même les événements du clavier à l'écran sont également capturés.
    * Le module clavier prend en charge les raccourcis clavier complexes.
    * En utilisant ce module, nous pouvons écouter et envoyer des événements de clavier.
    * Il fonctionne à la fois sur les systèmes d'exploitation Windows et Linux.
"""

        # Télécharger le module : pip3 install keyboard
# Utilisation du module keyboard
import keyboard

# Il écrit le contenu en sortie
keyboard.write("GEEKS FOR GEEKS \n")

# écrit les caractère r, k et endofline   
keyboard.press_and_release('shift + r, shift + k, \n')
keyboard.press_and_release('R, K')
  
keyboard.wait('Ctrl') # il bloque jusqu'à ce que ctrl soit appuyé
