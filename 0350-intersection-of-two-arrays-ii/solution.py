class Solution(object):
    def intersect(self, nums1, nums2):
        freq = [0]*1001
        result = []

        for i in nums1:
            freq[i] += 1
        
        for i in nums2:
            if freq[i] > 0:
                result.append(i)
                freq[i] -=1

        return result
        
        
