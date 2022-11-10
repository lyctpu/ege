import math
import turtle

sum=0
l=[x for x in range(10)]
print(l)
print('/'*20)

ls=[str(x) for x in range(10)]
print(ls)
for x in range (len(ls)):
    print(ls[x],end=' ')
print()

la=[x for x in 'abcdefg']
print(la)

print('='*20)

for x in range (10):
    for y in range(10):
        print(str(x)+str(y))
print('+'*20)

for x in range (3):
    for y in range(3):
        for i in range(3):
            if x!=y!=i:
                print(str(x)+str(y)+str(i))
print('-'*20)

for x in range (10):
    print(f'123{str(x)}789')

stri='123'
for x in stri:
    sum+=int(x)
print(sum)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5),'\n')

st='123456789'
print(st[2:-2])
print(st[2:len(st)-2],'\n')

for i in range(10):
    print(bin(i)[2:], bin(i)[1], int(bin(i)[2:],2))
