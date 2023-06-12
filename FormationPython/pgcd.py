def pgcd(a, b):
    if(a%b==0):
        return b
    else:
       return pgcd(b, a%b)
#def pgcd(a,b):
 #   while b!=0:
  #      r=a%b
   #     a=b
    #    b=r
    #return a

d = pgcd(16,9)
print(d)

