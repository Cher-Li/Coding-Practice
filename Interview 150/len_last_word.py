class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # strip for non space char, then split into words, [-1] for last word
        return len(s.rstrip().split()[-1])