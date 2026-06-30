class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        left = 0
        right = 1
        pair = 0

        while right < len(nums):
            if left >= right :
                right = left +1
                continue 

            diff = nums[right]- nums[left]

            if diff < k:
                right +=1

            elif diff > k :
                left += 1
            
            else :
                pair +=1 

                left += 1
                right +=1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left += 1
                while right < len(nums) and nums[right] == nums[right -1]:
                    right +=1 
        
        return pair

        
