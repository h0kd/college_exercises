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
sum1=sum(list_1)
sum2=sum(list_2)
sum3=sum(list_3)
print(list_1,0,list_2,0,list_3,999)
print('first group:', noe1)
print('second group:', noe2)
print('last group:', noe3)
print('sum of the first group:', sum1,'sum of the second group:', sum2,'sum of the last group:', sum3)
print('the numbers of groups is 3')


# Leer varios grupos de números. Cada grupo de números tiene distintas cantidades de números. 
# Imprimir la sumatoria de cada grupo y al final la cantidad de grupos existentes. El separador de grupos es el cero. Use Flag .