class Solution(object):
    # corner case: "" -> []
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        current = []
        self.do(digits,0,dic,current,res)
        return res
        
    def do(self,digits,i,dic,current,res):
        if i == len(digits):
            if current:
                res.append("".join(current))
            return
        if digits[i] in dic:
            for c in dic[digits[i]]:
                current.append(c)
                self.do(digits,i+1,dic,current,res)
                current.pop()
        else:
            self.do(digits,i+1,dic,current,res)
        
        