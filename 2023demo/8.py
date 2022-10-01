count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                        count+=1
print(count)