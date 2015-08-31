class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        bit = 1
        while n > 0:
            for i in xrange(len(res)-1,-1,-1):
                res.append(res[i]^bit)
            bit = bit << 1
            n -= 1
        return res