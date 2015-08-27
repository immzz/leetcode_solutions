class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while n > 1:
            m = min(a[p2]*2,min(a[p3]*3,a[p5]*5))
            if a[p2] * 2 == m:
                p2 += 1
            if a[p3] * 3 == m:
                p3 += 1
            if a[p5] * 5 == m:
                p5 += 1
            n -= 1
            a.append(m)
        return a[-1]
            
            
        