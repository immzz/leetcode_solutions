class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        current = []
        visited = [False] * len(num)
        self.do(num,visited,0,current,result)
        return result
    def do(self,num,visited,i,current,res):
        if i == len(num):
            res.append(current[:])
            return
        for j in xrange(len(num)):
            if not visited[j]:
                visited[j] = True
                current.append(num[j])
                self.do(num,visited,i+1,current,res)
                current.pop()
                visited[j] = False
        