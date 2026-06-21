class Solution(object):
    def minPairSum(self, nums):
        n = len(nums)
        left =0
        right = n-1
        sum = 0
        max_sum =0
        nums.sort()

        while left < right :
            sum = nums[left] + nums[right]
            max_sum = max(sum,max_sum)

            left += 1
            right -= 1
        
        return max_sum


       
        
