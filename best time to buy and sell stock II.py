class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        res = 0
        for i in xrange(1,len(prices)):
            res += max(0,prices[i]-prices[i-1])
        return res