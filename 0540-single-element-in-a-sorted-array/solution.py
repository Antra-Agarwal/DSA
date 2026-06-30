class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        left = 1
        right = n-2


        if n ==1 :
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        while left <= right :
            mid = left + (right-left)//2

            # we are in left  
            if (mid % 2 == 1 and nums[mid] == nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid+1]):
                left = mid +1

            # we are in right
            else :
                right = mid -1
        
        return nums[left]
