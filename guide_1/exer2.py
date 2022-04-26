# ejer 2 leer 3 veces, 2 numeros e imprimir el mayor

z=1
while(z<=3): # aqui le dijimos que el numero z tiene que ser menor e igual a 3 por lo tanto si cambiara el 3 por otro numero me generaria un loop de los ciclos que yo quisiera
    x=int(input("X="))
    y=int(input("Y="))

    if(x>y):
        print("El mayor es el X=", x)
    else:
        print("EL mayor es el Y=", y)

    z=z+1 # el z se va sumando +1 hasta que llega a 3 

print("Fin.......")