import sys
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        min_sum = [0] * len(grid[0])
        min_sum[0] = grid[0][0]
        for i in xrange(1,len(grid[0])):
            min_sum[i] = min_sum[i-1]+grid[0][i]
        
        for i in xrange(1,len(grid)):
            new_min_sum = [sys.maxint] * len(grid[0])
            new_min_sum[0] = min_sum[0]+grid[i][0]
            for j in xrange(1,len(grid[0])):
                if new_min_sum[j-1] < min_sum[j]:
                    new_min_sum[j] = new_min_sum[j-1] + grid[i][j]
                else:
                    new_min_sum[j] = min_sum[j] + grid[i][j]
            min_sum[:] = new_min_sum[:]
        return min_sum[-1]

sol = Solution()
print sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])