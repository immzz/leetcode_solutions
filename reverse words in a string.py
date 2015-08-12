class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    
    #corner case: "   " -> ""
    #corner case: "abc   " -> "abc"
    #corner case: "  abc" -> "abc"
    
    def reverseWords(self, s):
        lens = len(s)
        mid = int((lens-1)/2)
        s = list(s)
        for i in xrange(mid+1):
            temp = s[i]
            s[i] = s[lens-1-i]
            s[lens-1-i] = temp
        starting = 0
        i = 0
        while i <  lens:
            if s[i] == ' ':
                if starting < i:
                    innermid = int((starting+i-1)/2)
                    for j in xrange(starting,innermid+1):
                        temp = s[j]
                        s[j] = s[i-1-j+starting]
                        s[i-1-j+starting] = temp
                starting = i+1
            i += 1
        innermid = int((starting+i-1)/2)
        for j in xrange(starting,innermid+1):
            temp = s[j]
            s[j] = s[i-1-j+starting]
            s[i-1-j+starting] = temp
        s_new = [None]*len(s)
        j = -1
        for i in xrange(len(s)):
            if not (s[i] == ' '):
                j += 1
                s_new[j] = s[i]
            elif (s[i] == ' ') and (j>= 0) and (not s_new[j] == ' '):
                j += 1
                s_new[j] = s[i]
        if j >= 0 and s_new[j] == ' ':
            j -= 1
        return "".join(s_new[:j+1])
        

sol = Solution()
a = list('   abc   ds   ')
print a
print sol.reverseWords(a)
