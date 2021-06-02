import math as m
def findprime(n,data):
    def isprime(i):
        s=int(m.sqrt(i))
        for j in range(2,s+1):
            if i%j==0:
                return 0
        return 1
    c=[]           
    for i in data:
        if isprime(i):
            c.append(i)
    return c
n=int(input())
data=list(map(int,input().split()))
fp=findprime(n,data)
print(*fp)
    

