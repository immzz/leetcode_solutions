class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in xrange(min(len(s),len(t))):
            if s[i] != t[i]:
                if len(s) > len(t):
                    return s[i+1:] == t[i:]
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i+1:]
        return len(s) == len(t)+1 or len(s)+1==len(t)