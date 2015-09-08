class Solution(object):
    # corner case: "aa" -> "aa"
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = (len(s)-1)/2
        if len(s) % 2 == 0:
            r = l + 1
        else:
            r = l
        max_length = 0
        max_position = []
        while l >= 0:
            l_res = self.palindromeDo(s,l-1,l+1)
            if l_res[1] - l_res[0] + 1 > max_length:
                max_length = l_res[1] - l_res[0] + 1
                max_position = l_res[:]
            l_res = self.palindromeDo(s,l,l+1)
            if l_res[1] - l_res[0] + 1 > max_length:
                max_length = l_res[1] - l_res[0] + 1
                max_position = l_res[:]
            l_res = self.palindromeDo(s,r-1,r+1)
            if l_res[1] - l_res[0] + 1 > max_length:
                max_length = l_res[1] - l_res[0] + 1
                max_position = l_res[:]
            l_res = self.palindromeDo(s,r,r+1)
            if l_res[1] - l_res[0] + 1 > max_length:
                max_length = l_res[1] - l_res[0] + 1
                max_position = l_res[:]
            r += 1
            l -= 1
        return s[max_position[0]:max_position[1]+1]

    def palindromeDo(self,s,l,r):
        while l >=0 and r<len(s):
            if not s[l] == s[r]:
                break
            l -= 1
            r += 1
        return (l+1,r-1)

sol = Solution()
print sol.longestPalindrome("aa")
        
        