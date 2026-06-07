class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)

        maxi = float('-inf')
        sum = 0

        start = 0
        ans_start = 0
        ans_end = 0

        for i in range(n):
            sum += nums[i]

            if sum > maxi:
                maxi = sum
                ans_start = start
                ans_end = i

            if sum < 0:
                sum = 0
                start = i + 1

        print(nums[ans_start:ans_end + 1])  # maximum sum subarray
        return maxi
