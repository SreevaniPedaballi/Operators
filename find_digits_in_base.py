"""
Find no of digits in base b of number n
eg: log 10 base2
we can represent the log 10 base 2 as 10=2 raise to the power of 3.32
means 3(consider whole)+1 =total no of digits

formula: int(log of number n base b)+1
"""
from math import *

if __name__=="__main__":
    # n=42
    # b=2 
    # n=42
    # b=8
    n=42
    b=10
    digits=int(log(n)/log(b))+1
    print(digits)