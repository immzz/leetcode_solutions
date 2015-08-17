class Solution:
    # @param {integer[][]} costs
    # @return {integer}
    def minCost(self, costs):
        if not costs:
            return 0
        min_costs = [[sys.maxint for i in xrange(len(costs[0]))] for j in xrange(len(costs))]
        min_costs[0][:] = costs[0][:]
        for i in xrange(1,len(costs)):
            min_costs[i][0] = min(min_costs[i-1][1],min_costs[i-1][2])+costs[i][0]
            min_costs[i][1] = min(min_costs[i-1][0],min_costs[i-1][2])+costs[i][1]
            min_costs[i][2] = min(min_costs[i-1][0],min_costs[i-1][1])+costs[i][2]
        return min(min_costs[len(costs)-1][:])