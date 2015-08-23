class Solution(object):
    # corner case: "","" -> 0
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == len(needle):
                return i
        return -1 if not (haystack == "" and needle == "") else 0