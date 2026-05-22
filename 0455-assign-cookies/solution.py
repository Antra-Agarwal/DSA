class Solution(object):

    # Merge Sort
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result


    def findContentChildren(self, g, s):

        # Manual fast sorting
        g = self.mergeSort(g)
        s = self.mergeSort(s)

        # Two pointers
        i = 0
        j = 0
        count = 0

        while i < len(g) and j < len(s):

            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count
