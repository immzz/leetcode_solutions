class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) <= 2:
            return len(s)
        dic = {}
        dic[s[0]] = 0
        dic[s[1]] = 1
        current = 2
        max = current
        for i in xrange(2,len(s)):
            
            if (s[i] in dic) or (len(dic.keys()) == 1):
                dic[s[i]] = i
                current += 1
            else:
                char1,char2 = dic.keys()
                former = char1 if dic[char1] < dic[char2] else char2
                former_index = dic[former]
                del dic[former]
                dic[s[i]] = i
                current = i - former_index
            max = max if max > current else current
        return max