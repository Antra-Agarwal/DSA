class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        first = None
        second = None
        third = None

        for num in nums:

            # Skip duplicate numbers
            if num == first or num == second or num == third:
                continue

            # Update first maximum
            if first is None or num > first:
                third = second
                second = first
                first = num

            # Update second maximum
            elif second is None or num > second:
                third = second
                second = num

            # Update third maximum
            elif third is None or num > third:
                third = num

        # Return third maximum if exists
        if third is not None:
            return third
        else:
            return first
