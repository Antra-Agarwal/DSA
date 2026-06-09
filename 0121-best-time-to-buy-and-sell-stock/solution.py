class Solution(object):
    def maxProfit(self, prices):
        mini = prices[0]
        profit = 0
        n = len(prices)

        for i in range(1,n):
            cost = prices[i] - mini
            profit = max (profit,cost)
            mini = min(mini,prices[i])

        return profit

        
