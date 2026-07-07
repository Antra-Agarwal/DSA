class Solution(object):
    def shipWithinDays(self, weights, days):

        def canShip(capacity):
            daysUsed = 1
            currentWeight = 0

            for weight in weights:

                if currentWeight + weight <= capacity:
                    currentWeight += weight
                else:
                    daysUsed += 1
                    currentWeight = weight

            return daysUsed <= days

        low = max(weights)
        high = sum(weights)

        while low < high:

            mid = low + (high - low) // 2

            if canShip(mid):
                high = mid
            else:
                low = mid + 1

        return low
