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
listotal=[list_1,list_2,list_3] #edit
listotal2=len(listotal) #edit
noe1=len(list_1)
noe2=len(list_2)
noe3=len(list_3)
min1=min(list_1)
min2=min(list_2)
min3=min(list_3)
mintotal=min(min1,min2,min3)
if min1==mintotal:
    print('the minus number in all the groups is', mintotal, 'from the first group')
elif min2==mintotal:
    print('the minus number in all the groups is', mintotal, 'from the second group')
elif min3==mintotal:
    print('the minus number in all the groups is', mintotal, 'from the last group')
print(list_1,0,list_2,0,list_3,999)
print('first group:', noe1, 'elements')
print('second group:', noe2, 'elements')
print('last group:', noe3, 'elements')
print('the number of groups is', listotal2) #edit
#print('the numbers of groups is 3') #old line