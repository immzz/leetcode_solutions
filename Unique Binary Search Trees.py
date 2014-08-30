class Solution:
    sres = dict(([0,1],[1,1],[2,2]))
    
    # @return an integer
    def numTrees(self, n):
        if n in self.sres: return self.sres[n]
        sum = 0
        for i in range(n):
            sum = sum + self.numTrees(i)*self.numTrees(n-i-1)
        self.sres[n] = sum
        return sum
        