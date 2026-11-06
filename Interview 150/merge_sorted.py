class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # a ptr to keep track of current nums1 element, increment and insert wherever needed? 
        # maybe something like, when encounter somewhere to insert, swap with the next zero? <- deals w/ shifting so prolly not
        
        # * walk both from the end of the array and only keep the max from each
        write_index = m + n - 1 # * end of merged arr
        ptr1 = m - 1 # -1 not just m
        ptr2 = n - 1
        while ptr2 >= 0:
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                # nums1 has elements, current elmt > nums2's 
                nums1[write_index] = nums1[ptr1]
                ptr1 -= 1
            else:
                # place elmt from nums2 b/c larger or no more nums1
                nums1[write_index] = nums2[ptr2]
                ptr2 -= 1

            write_index -= 1