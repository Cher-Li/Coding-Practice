class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # so like, get that kth largest element, and make sure it's split up there? <- is nums even ordered
        # like what's stopping us from returning a summed version of nums[n - k:] and [0:n - k] or smt

        n = len(nums)
        k %= n
        # nums[:] = nums[-k:] + nums[:-k]
        # ig it's b/c it's O(N) space? 

        # another method: 
        def reverse(start, end): # don't put start: int typing
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1. Reverse whole array
        reverse(0, n - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse remaining n - k elements
        reverse(k, n - 1)
        # yea it's slower but better on mem