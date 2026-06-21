class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        output = []

        # Manual Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        x = 0

        while x < n - 3:
            left = x + 1

            while left < n - 2:
                y = left + 1
                right = n - 1

                while y < right:
                    total = nums[x] + nums[left] + nums[y] + nums[right]

                    if total == target:
                        output.append([nums[x], nums[left], nums[y], nums[right]])
                        y += 1
                        right -= 1

                    elif total < target:
                        y += 1

                    else:
                        right -= 1

                left += 1

            x += 1

        output = [list(item) for item in set(tuple(item) for item in output)]
        return output
