class Solution:
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.canSplit(nums, k, mid):
                ans = mid
                high = mid - 1   # Try to minimize the answer
            else:
                low = mid + 1    # Increase the allowed maximum sum

        return ans

    def canSplit(self, nums, k, maxSum):
        subarrays = 1
        currSum = 0

        for num in nums:
            if currSum + num <= maxSum:
                currSum += num
            else:
                subarrays += 1
                currSum = num

        return subarrays <= k
