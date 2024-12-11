"""
given number is a power of 2 or not
This works because in binary, a power of 2 has exactly one 1 bit
formula n & (n-1)=0 then its power of 2
"""
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Check for 152
print(is_power_of_two(152))  # Output: False
