class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in xrange(n)] for j in xrange(n)]
        i,j,dir,count = 0,0,0,0
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        for k in xrange(n*n):
            count += 1
            res[i][j] = count
            #print dirs,dirs[dir][0],i,j
            new_i,new_j = (i+dirs[dir][0]),(j+dirs[dir][1])
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or res[new_i][new_j] > 0:
                dir = (dir+1)%4
                new_i,new_j = i+dirs[dir][0],j+dirs[dir][1]
            i,j = new_i,new_j
        return res

        
sol = Solution()
print sol.generateMatrix(5)