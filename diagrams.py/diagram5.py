count=1
while count<=6:
    a=int(input("A="))
    b=int(input("B="))

    if a>b:
        b=b+3
        while a<5:
            a=a+1
            b=b+3
        else:
            a=a+4
            b=b+10

    else:
        print("A=", a,"B=", b)

    print(a,b)
    count+=1
    

print('end')