cost_punkt=[]
data=[]
konteiners=0
with open('27_A.txt') as f:
    d=f.readlines()
    punkts=d[0]
    
for i in range (1,len(d)):
    data.append(d[i].split())

for i in range (0,len(data)):
    position0=int(data[i][0])
    cost=0
    for y in range (0,len(data)):
        konteiners=round(int(data[y][1])/36)
        if round(int(data[y][1])/36) < int(data[y][1])/36:
            konteiners=(int(data[y][1])//36) + 1
        cost+=abs(int(data[y][0])-position0) * konteiners
        #print(f'cost={cost}  kont={konteiners}-{int(data[y][1])/36} разница пути пункта={abs(int(data[y][0])-position0)}')
    cost_punkt.append(cost)    
print(min(cost_punkt))
