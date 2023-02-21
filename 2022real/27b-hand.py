# дорога имеет взлеты и падения цены. Они плавные. Нужно методом сближения сужать диапазон поиска. Тот самый бинарный поиск. Здесь ручная модель подгонки.
# параметр start - позиция начала поиска, step-шаг поиска. значение в range - 100-это количество расчетов. В конце выдается вся табоица и находится минимальное, откуда можно и дальше сужать поиск
# все уже настроено на район правильного значения. Повторяющийся код для просмотра динамики, его можно и убрать
with open('27-B.txt') as f:
    c = [int(x) for x in f]
    c.pop(0)

#x = len(c) // step
c = c + c
summ = []
start = 40000
step = 100
zn = []
for i in range(100):#(x):
    su=0
    print(i)
    a = c[start+i*step:start+i*step + l]
    #a = c[start+i:start+i+l]
    # для первого(нулевого)
    for ii in range(len(a)):
        if ii > len(a) // 2:nomer = len(a) - ii
        else:nomer = ii - 0
        su=su+a[ii] * nomer
    summ.append(su)
    zn.append(start+i*step)
    #код ниже - просто повторение кода выше для посчета следующего пункта для просмотра динамики изменения
    su = 0
    aa = c[start + i * step+1:start + i * step + l+1]
    # a = c[start+i:start+i+l]
    # для первого(нулевого)
    for ii in range(len(aa)):
        if ii > len(aa) // 2:nomer = len(aa) - ii
        else:nomer = ii - 0
        su = su + aa[ii] * nomer
    summ.append(su)
    zn.append(start + i * step+1)

n=0
for i in summ:
    nn=step*(n//2)
    print(start+nn,i)
    n=n+1
print(min(summ),zn[summ.index(min(summ))]+1)
