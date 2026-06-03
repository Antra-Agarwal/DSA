class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        freq = [0] * (n+1)  
        output = []

        for i in nums:
            freq[i] += 1
        
        for j in range(1,n+1):
            if freq[j] == 0:
                output.append(j)
        
        return output
        
