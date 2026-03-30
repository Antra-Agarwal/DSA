class Solution(object):
    def missingNumber(self, nums):
       x = len(nums)
       expected_sum = x*(x+1)//2
       actual_sum = sum(nums)
       return( expected_sum - actual_sum)

nums = [3,0,1]
obj = Solution()
print(obj.missingNumber(nums))
