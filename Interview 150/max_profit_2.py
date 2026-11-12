class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # build off of if only one transaction, but this time when reaching a new day you can sell or buy if available? 
        # or like, literally just checking if one day is low and a future day is high, and just add to a running total

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1] # "telescoping sum"
            # and this works for prices = [1, 2, 3, 4, 5] when you're just selling on day 5 because it's still incrementally going through each day? 

        return profit