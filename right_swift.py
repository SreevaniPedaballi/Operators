"""

operator= >>

a >> b=a/(2 ** b)

2 >> 1= 2/(2 ** 1)=2/2=1
8>>2= 8/2 power2 =8/4=2

"""

if __name__=="__main__":
    print(2 >> 1)
    print(8 >> 2)