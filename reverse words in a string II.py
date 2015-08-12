class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        lens = len(s)
        mid = int((lens-1)/2)
        for i in xrange(mid+1):
            temp = s[i]
            s[i] = s[lens-1-i]
            s[lens-1-i] = temp
        starting = 0
        i = 0
        
        while i <  lens:
            if s[i] == ' ':
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
        

sol = Solution()
a = list('abc ds')
print a
sol.reverseWords(a)
print a