for a in range(1,1000):
    flag=True
    for x in range(1,100000):
        if ((x%2==0) <= (x%3!=0)) or (x+a>=100):
            flag=True
        else:
            flag=False
            break
    if flag==True: 
        print (a)
        break