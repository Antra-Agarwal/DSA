class Solution(object):

    def threeSum(self, nums):

        result = set()

        for i in range(len(nums)):

            seen = set()

            target = -nums[i]

            for j in range(i + 1, len(nums)):

                complement = target - nums[j]

                # If complement already seen
                if complement in seen:

                    triplet = [nums[i], nums[j], complement]

                    # Manual sorting of triplet (3 elements only)
                    if triplet[0] > triplet[1]:
                        triplet[0], triplet[1] = triplet[1], triplet[0]

                    if triplet[1] > triplet[2]:
                        triplet[1], triplet[2] = triplet[2], triplet[1]

                    if triplet[0] > triplet[1]:
                        triplet[0], triplet[1] = triplet[1], triplet[0]

                    result.add(tuple(triplet))

                seen.add(nums[j])

        return [list(x) for x in result]
