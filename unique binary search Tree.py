class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0] * (n+1)
        count[0],count[1] = 1,1
        self.do(n,count)
        return count[n]
    def do(self,n,count):
        if count[n] > 0:
            return count[n]
        res = 0
        for j in xrange(n):
            res += self.do(j,count)*self.do(n-1-j,count)
        count[n] = res
        return res