print('first group')
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
e=int(input('e='))
print('second group')
z=int(input('z='))
x=int(input('x='))
k=int(input('k='))
print('last group')
j=int(input('j='))
h=int(input('h='))
list_1=[a,b,c,d,e]
list_2=[z,x,k]
list_3=[j,h]
noe1=len(list_1)
noe2=len(list_2)
noe3=len(list_3)
max1=max(list_1)
max2=max(list_2)
max3=max(list_3)
print(list_1,0,list_2,0,list_3,999)
print('first group:', noe1)
print('second group:', noe2)
print('last group:', noe3)
print('max number 1=', max1,'max number 2=', max2,'max number 3=', max3)
print('the numbers of groups is 3')