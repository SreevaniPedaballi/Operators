"""
Find XR of numbers from 0 to n
0--0^0
1--0^1(s)
3--1^2
0--3^3
4--0^4(s)
1--4^5
7--1^6
0--7^7
8--0^8
1--8^8

n%4=0  n=n
n%4=1  n=1
n%4=2  n=n+1
n%4=3  0
"""
def xor_from_0_to_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:  # n % 4 == 3
        return 0

# Exnmple usnge
n = 7
print(f"XOR from 0 to {n} is {xor_from_0_to_n(n)}")
