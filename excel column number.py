class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        res = 0
        for i in xrange(len(s)):
            res *= 26
            res += ord(s[i]) - ord('A') + 1
        return res
            