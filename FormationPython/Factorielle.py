num = input("Entrer un nombre : ")
result = 1
def fact(val):
    x = int(val)
    if x == 0:
        return 1
    while x < 0:
        x = input("Entrer un nombre positif non nul: ")
        x = int(x)
    while not x == 0:
            global result 
            result *= x
            x -= 1
    print(result)
    
fact(num)



