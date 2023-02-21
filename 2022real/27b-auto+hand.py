with open('27-B.txt') as f:
    c = [int(x) for x in f]
    c.pop(0)

l=len(c)

summ = []
start = 0
step = 50000
x = len(c) // step
zn = []
c = c + c
for i in range(x):
    su=0
    a = c[start+i*step:start+i*step + l]
    # для первого(нулевого)
    for ii in range(len(a)):
        if ii > len(a) // 2:nomer = len(a) - ii
        else:nomer = ii - 0
        su=su+a[ii] * nomer
    summ.append(su)
    zn.append(start+i*step)

n=0
for i in summ:
    nn=step*n
    print(start+nn,i)
    n=n+1
print(min(summ),zn[summ.index(min(summ))]+1)

start = zn[summ.index(min(summ))]-step//2
finish=zn[summ.index(min(summ))]+step//2

step = 10000
while True:
    step = step // 4
    if step==0:step=1
    i = 0
    print(start, finish, step)
    input('Продолжаем')
    posit = start
    zn = []
    summ = []

    while posit<= finish:
        i+=1
        su = 0
        a = c[start+i*step:start+i*step + l]
        # для первого(нулевого)
        for ii in range(len(a)):
            if ii > len(a) // 2:nomer = len(a) - ii
            else:nomer = ii - 0
            su=su+a[ii] * nomer
        summ.append(su)
        zn.append(start+i*step)
        posit+=step
    n=0
    for i in summ:
        nn=step*n
        print(start+nn,i)
        n=n+1
    print(min(summ),zn[summ.index(min(summ))]+1)
    start = zn[summ.index(min(summ))] - step*2
    finish = zn[summ.index(min(summ))] + step*2
