class Solution(object):
    def minDays(self, bloomDay, m, k):

        #Impossible to make bouquets
        if m*k > len(bloomDay):
            return -1

        def canMake(day):
            no_bouquets = 0
            counter = 0

            for i in bloomDay:
                if i <= day :
                    counter += 1
                    
                    if counter == k:
                        no_bouquets += 1
                        counter = 0  # Reset counter because these flowers are used 
                else :
                    counter = 0
            return no_bouquets >= m
        
        low = min(bloomDay)
        high = max(bloomDay)

        while low < high :
            mid = low +(high-low)// 2

            if canMake(mid):
                high = mid
            else :
                 low = mid+1
        return low

        
        
