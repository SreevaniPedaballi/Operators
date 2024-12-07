"""
Start with the decimal number.
Repeatedly divide the number by 2.
Record the remainder at each step (it will be 0 or 1).
The binary representation is the remainders read from bottom to top.
"""
def convert_decimal_to_binary(num):
    bin=""
    while num>0:
        bin= str(num%2)+bin
        num=num//2
    return bin or 0
def convert_decimal_to_binary_m2(num):
    if num ==0:
        return ""
    return convert_decimal_to_binary_m2(num//2)+str(num%2)
def convert_decimal_to_binary_m3(num):
    return bin(num)[2:]
if __name__=="__main__":
    print(convert_decimal_to_binary(42))
    print(convert_decimal_to_binary_m2(42))
    print(convert_decimal_to_binary_m3(42))
