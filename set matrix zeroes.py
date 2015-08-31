class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        fr,fc = False,False
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        fr = True
                    else:
                        matrix[i][0] = 0
                    if j == 0:
                        fc = True
                    else:
                        matrix[0][j] = 0
                    
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if fr:
            for i in xrange(len(matrix[0])):
                matrix[0][i] = 0
        if fc:
            for j in xrange(len(matrix)):
                matrix[j][0] = 0
        
        
                    
                    
        