class Solution:
    # @param {integer} x
    # @return {integer}
    # corner case: 0 -> 0
    # corner case: 1 -> 1
    # corner case: 2 -> 1
    def mySqrt(self, x):
        l = 0
        r = x
        while True:
            mid = (l+r)/2
            dev = mid**2-x
            if dev < 0 and (mid+1)**2-x > 0:
                return mid
            elif dev > 0:
                r = mid
            elif dev < 0:
                l = mid+1
            else:
                return mid
        return mid

sol = Solution()
print sol.mySqrt(2)