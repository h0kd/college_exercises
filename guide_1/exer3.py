# ejer 3 concepto de flag ===> 999
# leer n= 1,2,3
# uso for

for var1 in range(1,999999999):
    x=int(input("X="))
    y=int(input("Y="))
    if(x!=999)and(y!=999):
        if(x>y):
            print("El mayor es el X=", x)
        else:
            print("EL mayor es el Y=", y)
    else:
        break

print("Fin.......")