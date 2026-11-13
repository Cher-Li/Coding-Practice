class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # maybe greedy? 
        max_reach = 0
        
        for i in range(len(nums)):
            # if current index further than max reach, stuck
            if i > max_reach:
                return False
            
            # update furthest index can reach from here
            max_reach = max(max_reach, i + nums[i])
            
            # early exit if can reach / surpass final index (b/c yes can surpass if just decrease the final jump length)
            if max_reach >= len(nums) - 1:
                return True
                
        return True