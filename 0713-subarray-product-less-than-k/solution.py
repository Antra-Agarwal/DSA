class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        result = 0
        left = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]

            while left <= right and product >= k:
                product = product // nums[left]
                left += 1
            
            result += right - left +1
        
        return result
       
