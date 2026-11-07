class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # non decreasing order so don't have to worry abt interweaving elements
        if not nums:
            return 0

        i = 1  # position for next unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i