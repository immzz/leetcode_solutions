class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        adj_list = [[] for _ in xrange(n)]
        visited = [False]*n
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        self.traverse(visited,adj_list,0)
        return all(visited)
        
    def traverse(self,visited,adj_list,i):
        visited[i] = True
        for j in adj_list[i]:
            if not visited[j]:
                self.traverse(visited,adj_list,j)
        
sol = Solution()
print sol.validTree(5, [[0,1],[0,4],[1,4],[2,3]])