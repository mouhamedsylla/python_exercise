from random import randint
from random import choice

score = 0
for i in range (0, 5):
    nbAlea1 = randint(0, 10)
    nbAlea2 = randint(0, 10)
    op = choice('*' '+' '-')

    if op == '+':
        r = nbAlea1 + nbAlea2
    elif op == '*':
        r = nbAlea1 * nbAlea2
    elif op == '-':
        r = nbAlea1 - nbAlea2

    result = input(f"Que vaut {nbAlea1} {op} {nbAlea2} : ")

    if int(result) == r:
        print("Correct!!!")
        score += 1
    else:
        print("Incorrect")
print("Votre score est de : "+str(score)+"/5")