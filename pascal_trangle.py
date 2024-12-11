"""
sum of nth row in pascal triangle

1
11
121
1331
14641

sum of 2nd row is 2

formula : 2 power n-1=(2**(n-1)) 
this is equal to 1 << n-1=(1*(2 **(n-1)))
"""


n=5
ans=1 << n-1

print(ans)