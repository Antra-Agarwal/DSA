class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        minimum = float('inf')

        while left <= right:
            
            mid = left + (right - left) // 2

            # Entire current range is sorted
            if nums[left] <= nums[right]:
                minimum = min(minimum, nums[left])
                break

           

            # Left half is sorted
            if nums[left] <= nums[mid]:
                minimum = min(minimum, nums[left])
                left = mid + 1

            # Right half is sorted, pivot is in left half
            else:
                minimum = min(minimum, nums[mid])
                right = mid - 1

        return minimum
