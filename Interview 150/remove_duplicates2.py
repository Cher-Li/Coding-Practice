class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is essentially the same as the previous remove duplicates prob just w/ write index starting at 2 and comparing two steps
        if len(nums) <= 2:
            return len(nums)

        k = 2  # first two elements are always allowed

        for i in range(2, len(nums)):
            # if equal to k - 2, just skip, otherwise new value to put at k
            if nums[i] != nums[k - 2]: # ordered so don't need to check k - 1
                nums[k] = nums[i]
                k += 1

        return k