#26
with open('26.txt') as f:
    data=f.readlines()
N=int(data[0])
del data[0]
for i in range(N):
    data[i]=int(data[i])
data.sort(reverse=True)

count=1
current=0
print(data[current])
for i in range(0,N-1):
    if abs(data[current]-data[i+1])>=3:
        current=i+1
        count+=1
        print(data[current], count)
print(count)
print(f'минимальная длина, которой можно заменить последнюю коробку {min(data)}')
