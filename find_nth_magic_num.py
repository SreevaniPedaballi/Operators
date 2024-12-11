"""
find nth magic number
base=5
1	001=0*5 **3+0*5**2+1*5 ** 1=5
2	010=10
3	011=15
4	100=125
5	101=130
6	110=135

if they ask you to find 5th magic number the the answer is 130

solution:
n=6

6th binary form=110
1.first take last digit that is 0*5 **1=5
2.next take remaining bits except the last one that is 11
3.repeat step1 and 2
"""

# def find_magic_num(n):
#     if n==0:
#         return 0
#     ans=0
#     base=5
#     while n>0:
#         last= n&1
#         n= n >> 1
#         ans+=last*base
#         base =base*5

#     return ans

def find_magic_num(num):
    if num==0:
        return num
    ans=0
    base=5
    while num >0:
        last=num&1
        num=num >> 1
        ans=last*base
        base=base*5

    return ans    

if __name__=="__main__":
    print(find_magic_num(4))
