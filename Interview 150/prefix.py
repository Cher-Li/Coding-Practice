class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # I mean brute force is just, match each first letter until one of them is different, but would have to keep indexing all the words? 

        if not strs:
            return ""

        prefix = strs[0] # first word

        for s in strs[1:]: # for each next word
            while not s.startswith(prefix): 
                prefix = prefix[:-1] # just keep chipping down the prefix until viable for both words
                if not prefix:
                    return ""

        return prefix

        # ok yea the vertical approach:
        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for s in strs[1:]:
        #         # stop if word shorter than i or char differ
        #         if i == len(s) or s[i] != char:
        #             return strs[0][:i]

        # return strs[0]