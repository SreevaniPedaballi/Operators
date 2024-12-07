
def binary_to_decimal(num):
    """
    In Python, enumerate() is a built-in function that adds a counter to an iterable 
    (such as a list, tuple, or string) and returns it as an enumerate object. 
    This is often used in loops when you need both the index and the value of 
    each item in the iterable.
    """
    decimal_num=0
    for i,bit in enumerate(reversed(num)):
        decimal_num+=int(bit)*(2 ** i)
    return decimal_num

"""
101010

int(0+2*(10101))=0+2*21=42
int(1+2*(1010))=1+2*10=21
int(0+2*(101))=0+2*5=10
int(1+2*(10)))=1+2*2=5
int(0+2*(1))=0+2=2
"""
def convert_binary_to_decimal_recursive(num):
    if not num:
        return 0
    return int(num[-1])+2*convert_binary_to_decimal_recursive(num[:-1])

if __name__=="__main__":
    print(binary_to_decimal("101010"))
    print(convert_binary_to_decimal_recursive("101010"))