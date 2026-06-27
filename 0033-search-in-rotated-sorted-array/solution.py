class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        ans = -1

        for i in range(n):
            if nums[i] == target :
                ans = i
        
        return ans
                
        
