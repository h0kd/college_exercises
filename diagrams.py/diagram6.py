a=int(input("A="))
b=int(input("B="))
c=int(input("C="))

for var1 in range(1,a):
    c=c+1
    for var2 in range(1,b):
        c=c+1
        a=a+2
print(a,b,c)
print('end')