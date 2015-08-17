class Solution:
    # @param {integer} n
    # @return {boolean}
    # corner case: 1 -> True
    # corner case: 0 -> False
    # corner case: -16 -> False
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n == 0:
            return False
        if n < 0:
            return False
        while n > 1:
            if n%2 != 0:
                return False
            n = n/2
        return True