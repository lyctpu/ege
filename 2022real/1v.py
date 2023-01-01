def ff():
    '''
    2-6.03
    4-8.47
    5-15.17
    6-19.58
    7-24.06
    8-27.33
    9-33.25
    11-39.20
    12-41.03
    14-46.54
    16-50.25
    17-55.53
    18-58.26
    22-1.05.35
    24-1.09.31
    25-1.12.08
    27-1.32.24
    '''
def f5(): # f'{x:09_b}'
    for N in range(516):
        b=f'{N:b}'
        if N%2==0: b+='10'
        else:b='1'+b+'01'
        if int(b,2)>516:
            print(N)
            break
def f6():
    for x in range(10000):
        s=x
        s=(s-10)//7
        n=1
        while s>0:
            n*=2
            s-=n
        if n==8:
            print(x)
            break
def f12():
    s='8'*86
    while '1111' in s or '8888' in s:
       if '1111' in s: s=s.replace('1111','8',1)
       else: s=s.replace('8888','11',1)
    print(s)

def f14():
    x=3*16**2018-2*8**1028-2**1050-2-2022
    c=0
    while x>0:
        c+= x%4 == 3
        #c=c+ (x%4 == 3)
        
        x//=4
    print(c)    

def f15():
    for A in range(100):
        if all(((x%3==0) <= (x%5!=0)) or (x + A >=70) 
               for x in range(1,10000)):
            print(A)
            break
        #all((x%3==0 <= (x%5!=0)) or (x + A >=70) 

def f17():
    with open('17.txt') as f:
        n=[int(x) for x in f]
    mn=min(x for x in n if x % 17==0)
    sums=[]
    for a, b in zip(n,n[1:]):
        if a % mn==0 or b % mn==0:
            sums.append(a+b)
    print(len(sums),max(sums))

def f19():
    from functools import lru_cache
    @lru_cache(None)
    def g(a,b):
        if a+b>=223:
            return 0
        ms=[(a*2,b),(a,b*2),(a+1,b),(a,b+1)]
        if any(g(x,y) ==0 for x,y in ms):
            return 1
        if all(g(x,y) ==1 for x,y in ms):
            return 2
        if any(g(x,y) ==2 for x,y in ms):
            return 3
        if all(g(x,y) in (1,3) for x,y in ms):
            return 4
    for x in range(1,205):
        if g(17,x)==3:
            print(3,x)
    for x in range(1,205):
        if g(17,x)==4:
            print(4,x)
        
def f22():
    for x in range(100000):
        s=x
        P=10
        Q=8
        K1=0
        K2=0
        while s<=100:
            s+=P
            K1+=1
        while s>=Q:
            s-=Q
            K2+=1
        K1+=s
        K2+=s
        if K1==10 and K2==19:
            print(x)
            break
            
        
def f24():   
    s=open('24.txt').readline().replace('AB','1').replace('AC','1')
    s=s.replace('A', '').replace('B',' ').replace('C',' ')
    print(max(len(x) for x in s.split()))
    
def f25():
    for a in range(10):
        for b in range(10):
            x=int(f'12345{a}6{b}8')
            if x%17==0:
                print(x,x//17)

def f27():
    with open('27-B.txt') as f:
        n=int(f.readline())
        m=([int(x) for x in f][:n]*3)[n//2:-n//2]
    print(0,m)
    
    pr=[0]*(len(m)+1)
    for i in range(1, len(pr)):
        pr[i]=pr[i-1]+m[i-1]
    
    po=[0]*(len(m)+1)
    for i in range(len(po)-2, -1,-1):
        po[i]=po[i+1]+m[i]
    print(pr)
    print(po)
    st=[0]*n
    fn=[0]*n
    st[0]=sum(pr[:n//2+1])
    fn[0]=sum(po[-n//2:])
    s1=s2=0
    
    for i in range(1,n):
        s1=m[i-1]*(n//2)+pr[i]
        s2=m[-i]*(n//2-1)+po[-i-1]
        st[i]=st[i-1]+pr[n//2+i]-s1
        fn[-i]=fn[(-i+1)%n]+po[-(n//2+i)]-s2
    c=0
    m=float('inf')
    for i,t in enumerate(zip(st,fn),start=1):
        if sum(t)<m:
            c,m=i,sum(t)
    print(c,a)    
    
f27()

