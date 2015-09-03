class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]
        used = [False] * n
        self.do(used,count,0,n)
        return count[0]
    def do(self,used,count,current,n):
        if current == n:
            count[0] += 1
            return
        for i in xrange(1,n+1):
            if not used[i-1]:
                used[i-1] = True
                self.do(used,count,current+1,n)
                self.do(used,count,current+1,n)
                used[i-1] = False
                