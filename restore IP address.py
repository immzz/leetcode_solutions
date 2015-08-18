class Solution:
    # @param {string} s
    # @return {string[]}
    # corner case: "010010" -> ["0.10.0.10","0.100.1.0"]
    def restoreIpAddresses(self, s):
        if len(s) > 12:
            return []
        res = []
        current = []
        self.do(s,0,current,res)
        return res
    def do(self,s,i,current,res):
        if len(current) == 4 and i == len(s):
            res.append(".".join(current))
        if i >= len(s):
            return
        for x in xrange(i,i+3):
            if int(s[i:x+1]) <= 255 and not (s[i] == '0' and i!=x):
                current.append(s[i:x+1])
                self.do(s,x+1,current,res)
                current.pop()
sol = Solution()
print sol.restoreIpAddresses("010010")
        