class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # maybe 2 pointers, left and right <- well maybe better for finding the max water instead

        # * O(N) time, if left_max <= right_max, at left ptr, know that whatever is to the right of left has a maximum height of at least right_max
        # left_max is bottleneck for left so don't need to scan between
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] # keep updating left_max
                else: # height[left] < left_max 
                    total_water += left_max - height[left]

                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right] # similar to left, update
                else: # height[right] < right_max
                    total_water += right_max - height[right]
                right -= 1

        return total_water

        # # so brute force, want to find all the "valleys" and just continue to add up until the end
        # n = len(height)
        # if n < 3:
        #     return 0

        # # water sit on top of height[i] up to the shorter of the tallest bar to its left and the tallest bar to its right, and if peak, no water
        # total_water = 0
        # for i in range(n):
        #     left_max = max(height[: i + 1])
        #     right_max = max(height[i:])
        #     trapped = min(left_max, right_max) - height[i]
        #     if trapped > 0:
        #         total_water += trapped

        # return total_water