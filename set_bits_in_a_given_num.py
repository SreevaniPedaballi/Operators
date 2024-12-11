"""
Find set bits in a given number

input 9
output is 2

here 9 binary representation is 1001 and it has 2 1s or set bits
"""

def method3(n):
    cnt=0
    while n>0:
        cnt+=1
        n -=(n & -n)
    return cnt
def method2(n):
    cnt=0
    while n>0:
        cnt+=1
        n=n & (n-1)
    return cnt

def method1(n):
    cnt=0
    while n>0:
        if n&1==1:
            cnt+=1
        n= n >> 1
    return cnt

n=91
print(bin(n)[2:])
print(method1(n))
print(method2(n))
print(method3(n))

