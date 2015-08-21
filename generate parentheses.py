class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        current = []
        res = []
        self.do(n,n,current,res)
        return res
        
    def do(self,left,right,current,res):
        if right == 0:
            res.append("".join(current))
            return
        if left:
            current.append('(')
            self.do(left-1,right,current,res)
            current.pop()
        if right > left:
            current.append(')')
            self.do(left,right-1,current,res)
            current.pop()