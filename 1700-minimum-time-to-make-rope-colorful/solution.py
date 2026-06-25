class Solution(object):
    def minCost(self, colors, neededTime):
        n = len(colors)
        time = 0
        for i in range(n-1):
            if colors[i] == colors[i+1]:

                if neededTime[i] < neededTime[i+1]:
                    time += neededTime[i]
                else :
                    time += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
        
        return time

       
        
