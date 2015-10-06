class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)-1,-1,-1):
            c = s[i]
            if c == 'I':
                res += -1 if res >= 5 else 1
            elif c == 'V':
                res += 5
            elif c == 'X':
                res += -10 if res >= 50 else 10
            elif c == 'L':
                res += 50
            elif c == 'C':
                res += -100 if res >= 500 else 100
            elif c == 'D':
                res += 500
            elif c == 'M':
                res += 1000
        return res
    