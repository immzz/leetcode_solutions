class Solution:
    # @param {string} s
    # @return {integer}
    
    # corner case: abba -> 2
    # corner case: aab -> 2
    # corner case: dvdf -> 3
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        start = 0
        dic = {}
        max = 1
        for i in xrange(len(s)):
            if (s[i] in dic) and (dic[s[i]] >= start):
                start = dic[s[i]] + 1
            current = i - start + 1
            dic[s[i]] = i
            max = max if max > current else current
        return max

sol = Solution()
print sol.lengthOfLongestSubstring("abba")
