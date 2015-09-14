class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if k == 1:
            return 1 if n <= 2 else 0
        if n == 1:
            return k
        adj,noadj = [1]*(n),[1]*(n)
        for i in xrange(1,n):
            adj[i] = noadj[i-1]
            noadj[i] = noadj[i-1]*(k-1)
        res = k*noadj[-1]
        for i in xrange(1,n):
            res += k*(adj[i]*((k-1)**(n-i-1)))
        return res

1 1 1 1 
1 1 1 1

1 1
1 1