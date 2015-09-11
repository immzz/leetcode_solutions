class Solution(object):
    # corner case: [1,1] -> 2
    # corner case: [2,1,2] -> 3
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = [(0,0)]
        res = 0
        for i in xrange(len(height)):
            h = height[i]
            start = i
            while s[-1][0] > h:
                prev = s.pop()
                start = prev[1]
                res = max((i-prev[1])*prev[0],res)
            if h > s[-1][0]:
                s.append((h,start))
        while s:
            res = max((len(height)-s[-1][1])*s[-1][0],res)
            s.pop()
        return res
    
sol = Solution()
print sol.largestRectangleArea([2,1,2])