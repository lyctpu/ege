#27B часть загрузки данных
cost_punkt=[]
data=[]
konteiners=0
with open('27_B.txt') as f:
    d=f.readlines()
    punkts=d[0]
    
for i in range (1,len(d)):
    data.append(d[i].split())
print(punkts)

#вторая часть программы методом половинного деления в ручном управлении
mini=1000000000
num_pu=0
count_i=0
ii=549724
for i in range(ii,ii+2):
    position0=int(data[i][0])
    cost=0
    for y in range (0,len(data)):
        konteiners=round(int(data[y][1])/36)
        if round(int(data[y][1])/36) < int(data[y][1])/36:
            konteiners=(int(data[y][1])//36) + 1
        cost+=abs(int(data[y][0])-position0) * konteiners
    print(cost)
