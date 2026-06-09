class Solution(object):
    def reverseByType(self, s):

        s = list(s)

        # Reverse letters
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not ('a' <= s[left] <= 'z'):
                left += 1

            while left < right and not ('a' <= s[right] <= 'z'):
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Reverse special characters
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and ('a' <= s[left] <= 'z'):
                left += 1

            while left < right and ('a' <= s[right] <= 'z'):
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
