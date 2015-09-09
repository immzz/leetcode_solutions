# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    # corner case: {} -> None
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        dic = {}
        return self.cloneDo(node,dic)
    def cloneDo(self,node,dic):
        if node in dic:
            return dic[node]
        new_node = UndirectedGraphNode(node.label)
        dic[node] = new_node
        new_node.neighbors = [self.cloneDo(x,dic) for x in node.neighbors]
        return new_node
        