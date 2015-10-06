# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        res = 0
        for i in xrange(len(points)-1):
            count = 1
            dic = {}
            for j in xrange(i+1,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    count += 1
                    continue
                if points[i].x == points[j].x:
                    if 'ver' not in dic:
                        dic['ver'] = 1
                    else:
                        dic['ver'] += 1
                    continue
                slope = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                if slope not in dic:
                    dic[slope] = 1
                else:
                    dic[slope] += 1
            total = count + (max(dic.values()) if len(dic.values()) > 0 else 0)
            if total > res:
                res = total
        return res

sol = Solution()
print sol.maxPoints([Point(0,0),Point(0,0)])
