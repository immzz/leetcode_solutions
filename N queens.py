class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        m = [['.' for i in xrange(n)] for j in xrange(n)]
        res = []
        used_col = [False] * len(m)
        used_lt = [False] * (2 * len(m) - 1)
        used_rt = [False] * (2 * len(m) - 1)
        self.solveDo(res,0,m,used_col,used_lt,used_rt)
        return res
    def solveDo(self,res,i,m,used_col,used_lt,used_rt):
        #print i,used_col,used_lt,used_rt
        if i == len(m) - 1:
            for j in xrange(len(m)):
                if self.check(used_col,used_lt,used_rt,i,j):
                    m[i][j] = 'Q'
                    res.append(["".join(x) for x in m])
                    m[i][j] = '.'
            return
        for j in xrange(len(m)):
            if self.check(used_col,used_lt,used_rt,i,j):
                m[i][j] = 'Q'
                self.set(used_col,used_lt,used_rt,i,j,True)
                self.solveDo(res,i+1,m,used_col,used_lt,used_rt)
                self.set(used_col,used_lt,used_rt,i,j,False)
                m[i][j] = '.'
    def set(self,used_col,used_lt,used_rt,i,j,val):
        used_col[j] = used_lt[i-j-1+len(used_col)] = used_rt[i+j] = val
    def check(self,used_col,used_lt,used_rt,i,j):
        return (not used_col[j]) and (not used_lt[i-j-1+len(used_col)]) and (not used_rt[i+j])
        
sol = Solution()
print sol.solveNQueens(8)