class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for i in xrange(numCourses)]
        in_count = [0]*numCourses
        added = [False] * numCourses
        path = []
        for edge in prerequisites:
            i,j = edge[0],edge[1]
            g[j].append(i)
            in_count[i] += 1
        while True:
            terminate = True
            for i in xrange(numCourses):
                if not added[i] and in_count[i] == 0:
                    terminate = False
                    path.append(i)
                    for j in g[i]:
                        in_count[j] -= 1
                    added[i] = True
                    break
            if terminate:
                break
        if sum(added) == numCourses:
            return path
        return []
        