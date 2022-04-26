a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
d=int(input("D="))
if a>b:
    a=a-1
    b=5
    if a>c:
        b=a
        d=c
    else:
        a=a+1
        b=b+2
        c=c+3
    d=d+1
else:
    a=a+10
    c=c+a
    b=b-1
    if b>d:
        a=a+b
        b=b+10
        c=c+15
    else:
        c=c+2
        b=b+c

print(a,b,c,d)
print('end')