class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        res = []
        while n > 0:
            res.insert(0,chr(((n-1) % 26)+ord('A')))
            n = (n-1) / 26
        return "".join(res)