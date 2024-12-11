
# # convert decimal to binary
deci_num=43
# print(bin(deci_num)[2:])

# # convert decimal to binary in iterative way
# bin=""
# while deci_num>0:
#     bin=str(deci_num%2)+bin
#     deci_num=deci_num//2
# deci_num=43
# print(bin)
# # convert decimal to binary in recursive way
# def dec_to_bin(num):
#     if num ==0:
#         return ""
#     return dec_to_bin(num//2)+str(num%2)
# print(dec_to_bin(deci_num))



#convert decimal to octal

# print(oct(deci_num)[2:])

# oct=""
# while deci_num>0:
#     oct=str(deci_num%8)+oct
#     deci_num=deci_num//8
# print(oct)

# deci_num=43
# def convert_deci_oct(num):
#     if num==0:
#         return ""
#     return convert_deci_oct(num//8)+str(num%8)

# print(convert_deci_oct(deci_num))

# dec=0
# for i, bin in enumerate(reversed("101010")):
#     dec += int(bin)*(2 ** i)
# print(dec)

def bin_dec(num):
    if not num:
        return 0
    return int(num[-1])+2*bin_dec(num[:-1])

print(bin_dec("101010"))