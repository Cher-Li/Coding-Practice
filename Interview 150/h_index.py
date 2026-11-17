class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # need at least h papers with at least h citations each
        # and keep incrementing h until like, the count of papers ordered in descending order passes the value of the citations

        citations.sort(reverse=True)

        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break

        return h