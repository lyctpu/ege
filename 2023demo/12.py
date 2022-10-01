spisok=[]
for n in range(1,1000):
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 and n%n**0.5!=0:
        print (n)
        spisok.append(n)
for i in spisok:
    for y in range (0,100):
        if y*4+117==i:
            print(y, i)