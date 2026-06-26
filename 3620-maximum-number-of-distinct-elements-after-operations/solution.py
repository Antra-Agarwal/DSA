class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()

        count_distinct= 0
        prevMax = float('-inf')

        for num in nums:
            lowerBound = num - k
            upperBound = num + k

            if prevMax < lowerBound:
                prevMax = lowerBound
                count_distinct += 1

            elif prevMax < upperBound:
                prevMax += 1
                count_distinct +=1

        return count_distinct
