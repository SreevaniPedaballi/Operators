"""
eg: input: num=[2,1,3,2,4,3,1]
output: ans:4

"""
def find_unique(num):
    if num==0:
        return 0
    unique=0
    for n in num:
        unique ^= n
    return unique

if __name__=="__main__":
    print(find_unique([2,1,2,1,3,3,2,8,3,1]))
