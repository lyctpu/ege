for i in range(41,100):
    #print(bin(i)[2:])
    z=str(bin(i)[2:])
    if z[0]+z[1]=='10' and z[len(z)-1]=='0':
        #z=z[0:len(z-2)]
        s=list(str(z[0:len(z)-1]))
        if s.count('1')%2!=0:
            s[1]='1'
        z=''
        for i in range (len(s)):
            z+=s[i]
        print(int(z,2), z)
    elif z[0]+z[1]=='11' and z[len(z)-1]=='1':
        #z=z[0:len(z-2)]
        s=list(str(z[0:len(z)-1]))
        if s.count('1')%2==0:
            s[1]='0'
        z=''
        for i in range (len(s)):
            z+=s[i]
        print(int(z,2), z)