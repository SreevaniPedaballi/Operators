"""
find power of given base
2 power2=4
3 power 6=729
"""

def power(base,power):
    ans=1
    while power >0:
        if power&1==1:
            ans *= base
        base *= base 
        power= power >>1
    return ans

print(power(3,6))
print(power(2,2))
