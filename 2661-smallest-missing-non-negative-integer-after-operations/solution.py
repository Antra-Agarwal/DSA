class Solution(object):
    def findSmallestInteger(self, nums, value):
        count = [0] * value

        
        for num in nums:
            remainder = num % value
            count[remainder] += 1

        mex = 0
        
        while count[mex % value] > 0:
            count[mex % value] -= 1
            mex += 1

        return mex

        
        
