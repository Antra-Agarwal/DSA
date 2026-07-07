class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        low = 0
        high = n-1

        while low <= high :
            mid = low +(high-low)//2
            missing = arr[mid] - (mid+1)
            
            if missing < k:
                low = mid +1

            else :
                high = mid -1    #ans = arr[high] + more 
                                   # more = k - missing
                                   # missing = arr[high] -(high +1)
                                   # ans = arr[high] + k - arr[high] + high + 1
                                   # ans = high + 1 + k
        return high +1 + k




