class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for token in tokens:
            try:
                s.append(int(token))
            except:
                if len(s) < 2:
                    return 0
                else:
                    op2 = s.pop()
                    op1 = s.pop()
                    if token == '+':
                        s.append(op1+op2)
                    elif token == '-':
                        s.append(op1-op2)
                    elif token == '*':
                        s.append(op1*op2)
                    elif token == '/':
                        if (op1 < 0) ^ (op2 < 0):
                            s.append(-(abs(op1)/abs(op2)))
                        else:
                            s.append(op1/op2)
        return s[0]

sol = Solution()
print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])




1  
1