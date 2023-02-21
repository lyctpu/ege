with open('27-A.txt') as f:
    #tab=map(int(x),f)
    c=[int(x) for x in f]
    c.pop(0)
print('Эталон')
print(c)
le=len(c)
p=len(c)//2
c=c+c
post=0
posit=0
for x in range(le):
    if x%100==0:print(x)
    d=c[x :le+x ]
    #print(d)
    pos=p+x+1
    #print(pos)
    p1=sum(d[:len(d)//2])
    if posit < p1:
        posit=p1
        positX=pos

x=positX-p-1
print('найденное')
d=c[x :le+x ]
#print(d)

posAV=len(d)//4
#print(d[posAV])
l=len(d)
ll=len(d)//2
d=d+d

mini=100000000000
print('новый код')

for ii in range(5):
    dd=[int(x) for x in d]
    dd=dd[l+posAV-ll-2+ii:l+posAV+ll-2+ii]
    pos=(len(dd)//2)-2+ii-1
    #print(pos)
    #print(dd)
    lis=[]
    le=len(dd)
    p=len(dd)//2
    for i in range(len(dd)):
        lis.append(abs(dd[i]*(p-i)))
    #print(lis)
    cost=sum(lis)
    print(cost)

    if cost<mini:
        mini=cost
        post=pos
if post>20: post=post-le
print(f'для {post} километра стоимость будет={mini}')
