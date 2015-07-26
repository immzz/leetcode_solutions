class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        s_dict = {}
        t_dict = {}
        if not (len(s) == len(t)):
            return False
        for i in range(len(s)):
            if ((s[i] in s_dict) and (t[i] not in t_dict)) or ((s[i] not in s_dict) and (t[i] in t_dict)):
                return False
            if ((s[i] in s_dict) and (t[i] in t_dict)) and not (s_dict[s[i]] == t_dict[t[i]]):
                return False
            s_dict[s[i]] = i
            t_dict[t[i]] = i
        return True

sol = Solution()
print sol.isIsomorphic('foo','bar')