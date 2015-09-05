class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s)
        s.sort()
        current = [None]*(len(s))*2
        res = []
        visited = [False] * len(s)
        self.do(s,current,res,0,visited,(len(s)-1)/2,(len(s)-1)/2+1)
        return res
    def do(self,s,current,res,i,visited,l,r):
        if i == len(s):
            res.append("".join(current[l+1:r]))
            return
        if i > len(s):
            return
        j = 0
        while j < len(s):
            if not visited[j]:
                if j == len(s) - 1 or s[j+1] != s[j]:
                    return
                visited[j] = visited[j+1] = True
                current[l] = s[j]
                current[r] = s[j]
                self.do(s,current,res,i+2,visited,l-1,r+1)
                visited[j] = visited[j+1] = False
                j += 2
                while j+1 < len(s) and s[j] == s[j-1] and s[j] == s[j+1]:
                    j += 2
            else:
                j += 2
                
sol = Solution()
print sol.generatePalindromes("aabb")