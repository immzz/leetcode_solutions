class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        count = 0
        current = 0
        res = 0
        for c in s:
            if c == '(':
                count += 1
                current += 1
            else:
                if count > 0:
                    count -= 1
                    current += 1
                    if count == 0:
                        res = max(res,current)
                else:
                    current = 0
        count,current = 0,0
        for i in xrange(len(s)-1,-1,-1):
            if s[i] == ')':
                count += 1
                current += 1
            else:
                if count > 0:
                    count -= 1
                    current += 1
                    if count == 0:
                        res = max(res,current)
                else:
                    current = 0
        return res