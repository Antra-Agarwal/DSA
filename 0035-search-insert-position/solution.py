class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
        output = 0 

        while left <= right :
            mid = left + (right-left)//2

            if target == nums[mid] :
                return mid
            elif target > nums[mid]:
                left = mid +1
            else :
                right = mid -1

        return left


        
