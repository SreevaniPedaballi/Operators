"""
XOR of all numbers between a to b
Eg:XOR of all numbers between 3 to 9
 3^4^5^6^7^8
"""

def xor(n):
    if n ==0:
        return 0
    if (n%4==0):
        return n
    elif(n%4==1):
        return 1
    elif(n%4==2):
        return n+1
    return 0

if __name__=="__main__":
    a=3
    b=9
    ans=xor(b)^xor(a-1)
    print(ans)

    ans1=0
    for i in range(a,b+1):
        ans1 ^= i
    print(ans1)