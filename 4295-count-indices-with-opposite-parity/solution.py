class Solution(object):
    def countOppositeParity(self, nums):
        n = len(nums)
        output = [0]*n  # using freq array

        for i in range(n):
            count = 0

            for j in range(i+1,n):
                if nums[i]%2 != nums[j]%2:
                    count += 1

            output[i]= count
        
        return(output)

