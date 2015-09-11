class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        H = [0] * len(matrix[0])
        res = 0
        for row in matrix:
            for i in xrange(len(row)):
                if row[i] == '1':
                    H[i] += 1
                else:
                    H[i] = 0
            print H
            res = max(res,self.largestRectangle(H))
        return res
        
    def largestRectangle(self,heights):
        res = 0
        s = [(0,0)]
        for i in xrange(len(heights)):
            start = i
            h = heights[i]
            while h < s[-1][0]:
                prev = s.pop()
                res = max(res,(i - prev[1])*prev[0])
                start = prev[1]
            if (not s) or (h != s[-1][0]):
                s.append((h,start))
        #print s
        while s:
            res = max(res,(len(heights)-s[-1][1])*s[-1][0])
            s.pop()
        return res
            
sol = Solution()
print sol.largestRectangle([4, 1, 4, 3])
#print sol.maximalRectangle(["1010","1011","1011","1111"])

'''
["1010"
,"1011"
,"1011"
,"1111"]
'''