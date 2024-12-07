def convert_decimal_to_octal_m1(num):
    return oct(num)[2:]
def convert_decimal_to_octal_m2(num):
    if num == 0:
        return num
    octal=""
    while num>0:
        octal=str(num%8)+octal
        num=num//8
    return octal or 0
def convert_decimal_to_octal_m3(num):
    if num == 0:
        return ""
    return convert_decimal_to_octal_m3(num//8)+str(num%8)
    
    
if __name__=="__main__":
    print(convert_decimal_to_octal_m1(42))
    print(convert_decimal_to_octal_m2(42))
    print(convert_decimal_to_octal_m3(42))
