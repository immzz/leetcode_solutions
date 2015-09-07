class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g = [[] for j in xrange(numCourses)]
        edge_count = [0] * numCourses
        for edge in prerequisites:
            g[edge[1]].append(edge[0])
            edge_count[edge[0]] += 1
        #print g
        eliminated = [False]*numCourses
        for k in xrange(numCourses):
            #print eliminated,edge_count
            terminate = True
            for i in xrange(numCourses):
                if not eliminated[i] and edge_count[i] == 0:
                    terminate = False
                    for out in g[i]:
                        edge_count[out] -= 1
                    eliminated[i] = True
                    break
            #print k
            if terminate:
                break
        #print eliminated
        return sum(eliminated) == numCourses

sol = Solution()
print sol.canFinish(2,[[1,0]])