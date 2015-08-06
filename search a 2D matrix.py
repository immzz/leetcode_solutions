class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        nrows = len(matrix)
        ncols = len(matrix[0])
        l = 0
        r = nrows*ncols-1
        current = None
        while l <= r:
            mid = int((l+r)/2)
            x = int(mid/ncols)
            y = mid - x*ncols
            current = matrix[x][y]
            if l == r:
                break
            if current < target:
                l = mid+1
            else:
                r = mid
        return current == target

sol = Solution()
print sol.searchMatrix([[1,3]], 3)