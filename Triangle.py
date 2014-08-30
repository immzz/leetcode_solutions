import sys
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        min_sum = [sys.maxint]*len(triangle)
        for row in range(0,len(triangle),1):
            if row == 0:
                min_sum[0] = triangle[0][0]
            else:
                min_sum[len(triangle[row])-1] = min_sum[len(triangle[row])-2]+triangle[row][len(triangle[row])-1]
                for col in range(len(triangle[row])-2,0,-1):
                    min_sum[col] = min(min_sum[col-1],min_sum[col])+triangle[row][col]
                min_sum[0] = min_sum[0]+triangle[row][0]
        return min(min_sum)
        
sol = Solution()
print sol.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])