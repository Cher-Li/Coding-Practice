class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        # I think this is like, want to buy on low, sell on high
        # keep a counter of max price
        current_min = prices[0]
        # for i in range(1, len(prices)):
        for price in prices[1:]: 
            current_profit = price - current_min
            max_profit = max(max_profit, current_profit)
            if price < current_min:
                current_min = price
        
        return max_profit