class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        current = []
        res = []
        self.do(1,n,0,k,current,res)
        return res
    def do(self,x,n,i,k,current,res):
        if i == k:
            res.append(current[:])
            return
        for j in xrange(x,n+1):
            current.append(j)
            self.do(j+1,n,i+1,k,current,res)
            current.pop()
        
sol = Solution()
print sol.combine(4,2)