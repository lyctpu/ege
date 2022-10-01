for x in range(15):
    first15=1*15**4+2*15**3+3*15**2+x*15**1+5
    second15=1*15**4+x*15**3+2*15**2+3*15+3
    sum10=first15+second15
    if sum10%14==0:
        print(x , sum10//14)   
        