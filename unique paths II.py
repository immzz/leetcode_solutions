class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        res = [[0 for i in xrange(len(obstacleGrid[0]))] for j in xrange(len(obstacleGrid))]
        for i in xrange(len(res[0])):
            if obstacleGrid[0][i] == 1:
                break
            res[0][i] = 1
        for i in xrange(1,len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if j > 0 and obstacleGrid[i][j-1] != 1:
                    res[i][j] = res[i][j-1]
                res[i][j] = res[i][j] if obstacleGrid[i-1][j] == 1 else res[i][j] + res[i-1][j]
        return res[len(res)-1][len(res[0])-1]

sol = Solution()
print sol.uniquePathsWithObstacles([[0]])