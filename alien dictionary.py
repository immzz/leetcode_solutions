class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        in_degree = {}
        out_edges = {}
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                if words[i][j] not in in_degree:
                    in_degree[words[i][j]] = 0
                    out_edges[words[i][j]] = []
        for i in xrange(1,len(words)):
            for j in xrange(min(len(words[i-1]),len(words[i]))):
                if words[i-1][j] != words[i][j]:
                    small_chr = words[i-1][j]
                    big_chr = words[i][j]
                    in_degree[big_chr] += 1
                    out_edges[small_chr].append(big_chr)
                    break
        res = []
        while in_degree:
            terminate = True
            key_to_delete = None
            for key in in_degree:
                val = in_degree[key]
                if val == 0:
                    key_to_delete = key
                    terminate = False
                    res.append(key)
                    for out_chr in out_edges[key]:
                        in_degree[out_chr] -= 1
                    break
            if terminate:
                break
            del in_degree[key_to_delete]
        if len(res) != len(out_edges):
            return ""
        return "".join(res)
        
                        
        
        
        