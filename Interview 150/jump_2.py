class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # similar to prev jump game, maybe try to take greedy jumps since can always reach n - 1? Not really since for ex 1, take a smaller jump first <- so need to be more involved, keep counter of smallest num of jumps overall? 

        # # dp approach, but N^2 overall
        # n = len(nums)
        # dp = [float('inf')] * n
        # dp[0] = 0

        # for i in range(1, n): 
        #     for j in range(i): # can possibly jump from any j to i 
        #         if j + nums[j] >= i:
        #             dp[i] = min(dp[i], dp[j] + 1) # min num jumps reach i from 0

        # return dp[-1]

        # dp values just keep increasing since counting up num steps, want to track rightmost boundary of jump lvl and find the furthest reach for next jump lvl
        jumps = 0
        current_end = 0
        farthest = 0

        # stop at len(nums) - 1 exclusive
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # reached end of current jump range, commit to next jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # if the new window already covers the end, stop
                if current_end >= len(nums) - 1:
                    break

        return jumps