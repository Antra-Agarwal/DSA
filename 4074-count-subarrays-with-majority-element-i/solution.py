class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        ans = 0

        for i in range(n):
            targetCount = 0
            otherCount = 0

            for j in range(i, n):
                if nums[j] == target:
                    targetCount += 1
                else:
                    otherCount += 1

                if targetCount > otherCount:
                    ans += 1

        return ans
