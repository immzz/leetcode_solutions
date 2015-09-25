class Solution(object):
    # corner case: "a","ab*"
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = [[None for _ in xrange(len(p))] for _ in xrange(len(s))]
        return self.matchDo(s,0,p,0,match)
        #print match
        
    def matchDo(self,s,i,p,j,match):
        #print i,j
        if i == len(s):
            if j == len(p):
                return True
            if j < len(p)- 1 and p[j+1] == '*':
                return self.matchDo(s,i,p,j+2,match)
            return False
        if j == len(p):
            return False
        if match[i][j] is not None:
            return match[i][j]
        if s[i] == p[j] or p[j] == '.':
            if j < len(p) - 1 and p[j+1] == '*':
                if self.matchDo(s,i+1,p,j,match):
                    match[i][j] = True
                    return True
                if self.matchDo(s,i+1,p,j+2,match):
                    match[i][j] = True
                    return True
                if self.matchDo(s,i,p,j+2,match):
                    match[i][j] = True
                    return True
            else:
                return self.matchDo(s,i+1,p,j+1,match)
        elif j < len(p) - 1 and p[j+1] == '*':
            if self.matchDo(s,i,p,j+2,match):
                match[i][j] = True
                return True
        match[i][j] = False
        return False

sol = Solution()
print sol.isMatch("a","ab*b*")
