class Solution(object):
    def majorityElement(self, nums):
        count = 0
        star = None

        for i in nums:
            if count == 0:
                star = i

            if i == star:
                count += 1
            else:
                count -= 1

        return star


nums = [2,2,1,1,1,2,2]

obj = Solution()
print(obj.majorityElement(nums))
