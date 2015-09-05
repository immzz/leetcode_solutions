class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        current = []
        count = [0]
        visited = [False] * n
        self.do(current,visited,n,0,k,count)
        return current
    def do(self,current,visited,n,i,k,count):
        #print count[0]
        if i == n:
            count[0] += 1
            return None
        for j in xrange(n):
            if not visited[j]:
                visited[j] = True
                current.append(j+1)
                res = self.do(current,visited,n,i+1,k,count)
                if count[0] == k:
                    return
                current.pop()
                visited[j] = False
            
sol = Solution()
print sol.getPermutation(9,2)