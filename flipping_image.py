"""
Google Question
eg: 
input:
1 0 1
0 1 0
1 1 0

output:
reverse:
1 0 1
0 1 0
0 1 1

final output:
0 1 0
1 0 1
1 0 0

Solution:
forst revers each row and do compliment means replace 0 with 1 and 1 with 0
"""

def flipping_image(arr):
    if(len(arr)==0):
        return 0
    for row in range(len(arr)):
        for col in range((len(arr[row])//2)+1):
            temp=(arr[row][col])^1 # swap 0 to 1 and 1 to 0
            arr[row][col]=(arr[row][len(arr[row])-1-col])^1
            arr[row][len(arr[row])-1-col]=temp
    return arr

if __name__=="__main__":
    # arr=[[1,1,0]]
    arr=[[0,1,0],[1,0,1],[1,0,0]]
    print("Input:")
    print(arr)
    print("Output:")
    print(flipping_image(arr))

            