class Solution(object):
    def returnToBoundaryCount(self, nums):
        n = len(nums)
        return_count = 0
        sum = 0

        for i in range(n):
            sum = sum + nums[i]

            if sum == 0:
                return_count += 1
        
        return return_count
        
