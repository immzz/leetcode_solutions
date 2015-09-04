class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        dic = {}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = [edge]
            else:
                dic[edge[0]].append(edge)
            if edge[1] not in dic:
                dic[edge[1]] = [edge]
            else:
                dic[edge[1]].append(edge)
        while True:
            for key,val in dic.items():
                if len(val) == 1:
                    
        