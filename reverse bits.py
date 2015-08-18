class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for x in xrange(32):
            res = (res << 1) | (n&1)
            n = n >> 1
        return res