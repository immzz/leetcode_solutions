class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    
    # corner case: "","","a"
    # corner case: "","a","a"
    # corner case: "aa", "ab", "aaba" "abc"
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        is_interleave = [[False for i in xrange(len(s2)+1)] for j in xrange(len(s1)+1)]
        is_interleave[0][0] = True
        for i in xrange(len(s1)+1):
            for j in xrange(len(s2)+1):
                if i==0 and j==0:
                    continue
                s = i+j-1
                is_interleave[i][j] = (i > 0 and s1[i-1] == s3[s] and is_interleave[i-1][j]) or (j > 0 and s2[j-1] == s3[s] and is_interleave[i][j-1])
        return is_interleave[len(s1)][len(s2)]
        

sol = Solution()
print sol.isInterleave("aa", "ab", "aaba")
                