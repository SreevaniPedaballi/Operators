"""

operator= <<
a << 1 will always 2a
a << 2 will always a*2 power 2

eg: 2 << 1=4(double)
2 << 2= (2 * 2 power 2 )= 2*4=8
"""

if __name__=="__main__":
    print(2 << 1)
    print(2 << 2)