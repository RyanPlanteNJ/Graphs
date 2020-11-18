"""
EVEN DIGITS
"""

class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digit = 0
            
            while num > 0:
                digit += 1
                num = int(num/10)
            if digit % 2 == 0:
                count += 1
        return count


"""
ISSUBMATRIXFULL
"""

def getCol(mat, col):
    return [mat[i][col] for i in range(3)]

def isSubMatrixFull(mat):
    n = len(mat[0])
    ans = [False]*(n-2)
    kernel = getCol(mat, 0) + getCol(mat, 1) + getCol(mat, 2) # O(1)
    for i in range(n - 2): # O(n)
        if len(set(kernel)) == 9: # O(1)
            ans[i] = True # O(1)
        if i < n - 3: # O(1)
            kernel = kernel[3:] + getCol(mat, i + 3) # O(1)
    return ans