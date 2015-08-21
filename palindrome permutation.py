class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        odd_count = 0
        for v in dic.values():
            if v % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True