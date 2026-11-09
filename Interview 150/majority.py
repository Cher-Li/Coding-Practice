class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force would be to count up all nums and return the one w/ greatest count? (or inner loop counting freq of arr[i]) Well it also has to be a count greater than n / 2

        # * voting alg
        n = len(nums)
        candidate = -1
        count = 0

        # find a candidate
        for num in nums:
            if count == 0:
                candidate = num
                count = 1 # essentially resetting after getting that candidate
            elif num == candidate:
                count += 1 # to check if greater than n/2 times
            else:
                count -= 1 # b/c all other elements less than n/2 times

        # validating the candidate
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > n // 2:
            return candidate
        else:
            return -1