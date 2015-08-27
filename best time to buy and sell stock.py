class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current = 0
        profit = 0
        for i in xrange(1,len(prices)):
            current = max(0,current + prices[i] - prices[i-1])
            profit = max(profit,current)
        return profit