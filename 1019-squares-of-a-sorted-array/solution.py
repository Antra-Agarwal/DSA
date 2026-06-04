class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        output = [0]*n
        left = 0
        right = n-1
        a = n-1

        while left <= right :
            if abs(nums[left]) < abs(nums[right]):
                output[a] = nums[right] * nums[right]
                right -= 1
                a -= 1
            else :
                output[a] = nums[left] * nums[left]
                left += 1
                a -= 1
        
        return output

