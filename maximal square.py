class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        if (not matrix) or (not matrix[0]):
            return 0
        m = 0
        for i in xrange(len(matrix)):
            res[i][0] = 1 if matrix[i][0] == '1' else 0
            m = max(m,res[i][0])
        for i in xrange(len(matrix[0])):
            res[0][i] = 1 if matrix[0][i] == '1' else 0
            m = max(m,res[0][i])
        
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix[i])):
                if matrix[i][j] == '0':
                    res[i][j] = 0
                    continue
                if matrix[i-1][j-1] == '0':
                    res[i][j] = 1
                    continue
                if res[i-1][j] >= res[i-1][j-1] and res[i][j-1] >= res[i-1][j-1]:
                    res[i][j] = res[i-1][j-1] + 1
                elif matrix[i-1][j] == '1' and matrix[i][j-1] == '1':
                    res[i][j] = 2
                else:
                    res[i][j] = 1
                m = max(m,res[i][j])
        #print res
        return m**2

a = \
["0001"
,"1101"
,"1111"
,"0111"
,"0111"]

[[0, 0, 0, 1]
,[1, 1, 0, 1]
,[1, 2, 1, 1]
,[0, 1, 1, 2]
,[0, 1, 2, 2]]

sol = Solution()
print sol.maximalSquare(a)