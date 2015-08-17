import sys
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    
    # corner case: "a", "a" -> "a"
    # corner case: "a", "aa" -> ""
    def minWindow(self, s, t):
        dic = {c:None for c in t}
        start = sys.maxint
        end = -1
        minstart = sys.maxint
        minend = -1
        min = sys.maxint
        for i in xrange(len(s)):
            if s[i] not in dic:
                continue
            dic[s[i]] = i
            all_filled = True
            current_min = sys.maxint
            current_max = -1
            for v in dic.values():
                if v is None:
                    all_filled = False
                else:
                    if current_min > v:
                        current_min = v
                    if current_max < v:
                        current_max = v
            if all_filled:
                end = current_max
                start = current_min
                if end - start < min:
                    min = end-start
                    minstart = start
                    minend = end
        if min == sys.maxint:
            return ""
        else:
            return s[minstart:minend+1]
            
sol = Solution()
print sol.minWindow("a", "a")