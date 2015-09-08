class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        for i in xrange(n):
            current = 0
            j = i
            while current + gas[j] >= cost[j]:
                current = current + gas[j] - cost[j]
                j = (j+1)%n
                if j == i:
                    return i
        return -1