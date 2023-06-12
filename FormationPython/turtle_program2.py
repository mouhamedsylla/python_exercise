import turtle

t = turtle.Turtle()
#Escalier

"""def escalier(pixel, nbmarge):
    t.forward(pixel)
    for i in range(0,nbmarge):
        
        t.left(90)
        t.forward(pixel)
        t.right(90)
        t.forward(pixel)
        

escalier(50,7)"""

#Carré

"""def carre(cote):
    t.forward(cote)
    for i in range(0,3):
        t.left(90)
        t.forward(cote)

carre(50)"""


#Plusieurs carrés
def carre(cote_depart, nbmotif):
    for i in range(1, nbmotif):
         cote = cote_depart * i
         for j in range(0,3):
            t.forward(cote)
            t.left(90)
            t.forward(cote)
            
    

carre(10, 30)
turtle.done()