class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows <= 0:
            return []
        triangle = [[1],]
        for i in xrange(1,numRows):
            current = [1]
            for j in xrange(1,i):
                current.append(triangle[i-1][j-1]+triangle[i-1][j])
            current.append(1)
            triangle.append(current)
        return triangle
            