count=0
itog=[]
itogost=[]
for i in range(10):
    for y in range(1000000):
        #нулевые символы
        chislo2='1'+str(i)+'21394'
        
        if int(chislo2)%2023==0:
            ost=int(chislo2)//2023
            print(chislo2, ost)
            itog.append(chislo2)
            itogost.append(ost)
            count+=1
            
        chislo='1'+str(i)+'2139'+str(y)+'4'
        if int(chislo)>10**10:break
        if int(chislo)%2023==0:
            ost=int(chislo)//2023
            print(chislo, ost)
            count+=1
            itog.append(chislo2)
            itogost.append(ost)
print(itog)
print(itogost)

        
        
