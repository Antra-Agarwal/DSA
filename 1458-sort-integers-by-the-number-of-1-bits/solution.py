class Solution:
    def countBits(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def sortByBits(self, arr):
        arr.sort(key=lambda x: (self.countBits(x), x))
        return arr
