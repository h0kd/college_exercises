z=1
n=int(input("N="))
while(z<=n): # aqui le dijimos que el numero z tiene que ser menor e igual a 3 por lo tanto si cambiara el 3 por otro numero me generaria un loop de los ciclos que yo quisiera
    x=int(input("X="))
    y=int(input("Y="))

    if(x>y):
        print("El menor es Y", y)
    else:
        print("El menor es X", x)

    z=z+1 # el z se va sumando +1 hasta que llega a 3 

print("Fin.......")