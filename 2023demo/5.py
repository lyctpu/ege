for i in range(41,100):
    #print(bin(i)[2:])
    z=str(bin(i)[2:])
    if z[0]+z[1]=='10' and z[len(z)-1]=='0':
        print(int(z,2), z)
    elif z[0]+z[1]=='11' and z[len(z)-1]=='1':
        print(int(z,2), z)