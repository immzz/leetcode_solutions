class Solution(object):
    # corner case: ".," -> True
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            while i<len(s) and not s[i].isalpha():
                i += 1
            while j >= 0 and not s[j].isalpha():
                j -= 1
            if (i<len(s) and j>=0) and not s[i] == s[j]:
                return False
            i += 1
            j -= 1
        return True