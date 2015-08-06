class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        l = len(matrix)
        for i in xrange(l):
            for j in xrange(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in xrange(len(matrix)):
            for j in xrange(int((l-1)/2)+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][l-1-j]
                matrix[i][l-1-j] = temp
        