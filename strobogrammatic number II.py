class Solution:
    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        digits  = ["00","11","69","88","96"]
        res  = [""] if n %2 == 0 else ["0","1","8"]
        while n >= 2:
            n -= 2
            res = [ first + x + second for first,second in digits[n<2:] for x in res]
        return res

sol = Solution()
print sol.findStrobogrammatic(3)