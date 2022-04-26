z=1
a=0
b=0
while(z==1):
    a=int(input("A="))
    b=int(input("B="))

    if(a!=999)and(b!=999):
        if(a>b):
            print("El menor es B=", b)
        else:
            print("El menor es A=", a)
    else:
        z=2

print("finish")