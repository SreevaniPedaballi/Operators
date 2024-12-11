"""
reset 4th bit(0 with 1 and 1 with 0)
n= 101010
ans=100010
if 1 is there at 4th place just keep it as 0 otherwise replace with 1
formula(n& compliment of (1<<(n-1)))
101010
110111
------
10010(ans)


Q: Find the position of the right most set bit
Ans: N & (-N)

1 byte=8 bits
in each bit we can store 0 or 1 so here 8 bits each with 2
2*2*2*2*2*2*2*2=2 power 8=256 unique numbers we can store in single byte
actual numbers stored in single byte is n-1(7 bits) and the remaing 1 bit is for representing +ve or -ve
 
actual value= 2 power 7=128
total unique numbs=256
 127 +ve and 128 -ve(0 includes)
 if the num 1010 here 1st bit that is 1 is most significant bit(MSB)
   and last digit that is 0 is Least significant bit(LSB)
   10= 00001010 here MSB is 0 so it is positive number if the MSB is 1 then it is a negative number

   convert 10 to -10(use 2s compliment method)
   1.get compliment of 10
   2.add 1

   10=           00001010
compliment of 10=11110101
+1=              00000001
-------------------------
                11110110


Range formula:
-2 power n-1 to 2 power n-1 -1

-2 **(n-1) to 2 ** (n-1)-1
"""

