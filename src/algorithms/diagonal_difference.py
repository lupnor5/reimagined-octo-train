

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum_ = 0
    for i in  range(n):
        sum_  += arr[i][(n-1)-i] - arr[i][i]
    return sum_  


print(diagonalDifference( [[6, 8],
[-6, 9]] 
))