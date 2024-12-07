
def convert_binary_decimal_recursive(num):
    if not num:
        return 0
    return int(num[-1])+2*convert_binary_decimal_recursive(num[:-1])

def convert_bin_to_deci(num):
    deci=0
    for idx,bit in enumerate(reversed(num)):
        deci += int(bit)*(2 ** idx)
    return deci
def convert_decimal_to_octal_r(num):
    if num==0:
        return ""
    return convert_decimal_to_octal_r(num//8)+str(num%8)
def convert_decimal_to_octal(num):
    deci=""
    while num>0:
        deci=str(num%8)+deci
        num=num//8
    return deci or 0

if __name__=="__main__":
    decimal_val=convert_bin_to_deci("101010")
    oct_val=convert_decimal_to_octal(decimal_val)
    print(oct_val)
    