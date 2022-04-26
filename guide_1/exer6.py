import statistics
z=1
n=int(input("N="))
while(z<=n): 
    x=int(input("X="))
    y=int(input("Y="))
    o=int(input("O="))

    list=[x,y,o]
    list.remove(min(list))
    print(list)
    mean=statistics.mean(list)
    print(mean)

    z=z+1 

print("Fin.......")