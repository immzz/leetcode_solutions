class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([n])
        while n != 1:
            new_n = 0
            while n > 0:
                digit = n % 10
                new_n += digit ** 2
                n = n / 10
            n = new_n
            if n in s:
                return False
            s.add(n)
        return True

sol = Solution()
print sol.isHappy(7)