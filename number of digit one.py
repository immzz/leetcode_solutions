class Solution(object):
    # 1. ones at this index
    # 2. ones at smaller index: in numbers less than 10**i; in numbers from 10**i to n
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print n
        i = 1
        while n/i >= 10:
            i *= 10
        if i == 1:
            return 1 if n > 0 else 0
        head = n/i
        if head == 1:
            return n%i+1+self.countDigitOne(i-1)+self.countDigitOne(n%i)
        else:
            return i+head*self.countDigitOne(i-1)+self.countDigitOne(n%i)

sol = Solution()
print sol.countDigitOne(13)