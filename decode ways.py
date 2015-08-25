class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic = {}
        A_index = ord('A')
        for i in xrange(26):
            dic[str(i+1)] = chr(A_index+i)
        count = [1]+[0]*len(s)
        for i in xrange(1,len(s)+1):
            if s[i-1] in dic:
                count[i] = count[i-1]
            if i-2>=0 and s[i-2:i] in dic:
                count[i] += count[i-2]
        return count[-1]
