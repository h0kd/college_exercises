z=1
n=int(input("N="))
while(z<=n): 
    x=int(input("X="))
    y=int(input("Y="))
    o=int(input("O="))

    if((x>y)and(x>o)):
        print("El mayor es X", x)
    elif((y>x)and(y>o)):
        print("El mayor es Y", y)
    elif((o>x)and(o>y)):
        print("El mayor es O", o)
    else:
        print("Salio mala la wea")

    z=z+1 

print("Fin.......")