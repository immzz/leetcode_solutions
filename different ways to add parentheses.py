class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in '-+*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for r1 in res1:
                    for r2 in res2:
                        if input[i] == '-':
                            res.append(r1-r2)
                        elif input[i] == '+':
                            res.append(r1+r2)
                        else:
                            res.append(r1*r2)
        return res