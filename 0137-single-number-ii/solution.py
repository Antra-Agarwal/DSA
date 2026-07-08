class Solution:
    def singleNumber(self, nums):
        nums.sort()
        n = len(nums)

        i = 0
        while i < n - 2:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3

        return nums[-1]
