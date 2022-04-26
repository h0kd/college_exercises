count=1
while count<=6: 
    a=int(input("A="))
    b=int(input("B="))
    c=int(input("C="))
    d=int(input("D="))
    if a>b:
        if a>c:
            if b>c:
                a=a+1
                b=a+3
                                 
            else:
                if a>d:
                    a=a+1
                    b=b+10
                    c=c+20
                    d=d+20

                else:
                    a=2
                    b=3
                    c=4
                    d=5

        else:
            for var1 in range(1,a):
                c=c+2
                d=d+3
               
            a=a+d
            b=a+c+d

    else:
        print("A=", a,"B=", b,"C=", c,"D=", d)

    print(a,b,c,d)

    count+=1

print('End')