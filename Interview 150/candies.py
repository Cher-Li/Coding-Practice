class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # I think this is like, left to right pass, make sure all children on the right with a higher rating gets more candies, then vice versa for the other direction, then count all the candies

        n = len(ratings)
        candies = [1] * n

        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1) # * 

        return sum(candies)