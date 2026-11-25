class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # valid roman numeral so just need to check where subtraction is used (aka a smaller one on the left of a bigger char), otherwise addition

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]] # just subtract the char placed before the bigger one
            else:
                total += values[s[i]]

        return total