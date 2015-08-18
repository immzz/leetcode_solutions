# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    
    # corner case: [[1,1],[1,1],[2,2],[2,2]] -> 4
    def maxPoints(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1
        max = 2
        for i in xrange(len(points)):
            if i == 0:
                continue
            current = 2
            if points[0].x == points[i].x:
                for j in xrange(1,len(points)):
                    if j == i:
                        continue
                    if points[j].x == points[i].x:
                        current += 1
                if current > max:
                    max = current
            else:
                a = float(points[0].y-points[i].y)/(points[0].x-points[i].x)
                b = points[i].y - a*points[i].x
                for j in xrange(1,len(points)):
                    if j == i:
                        continue
                    if points[i].x != points[j].x:
                        tempa = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                        tempb = points[i].y - tempa*points[i].x
                        if tempa == a and tempb == b:
                            current += 1
                    elif points[i].y == points[j].y:
                        current += 1
                if current > max:
                    max = current
        return max

ps = [Point(1,1),Point(1,1),Point(2,2),Point(2,2)]
sol = Solution()
print sol.maxPoints(ps)