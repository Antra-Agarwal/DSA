class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
         
        i, j = 0, 0
        result = []
         
        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1
            
            else:
                j += 1
        
        return result

nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersection(nums1,nums2))

