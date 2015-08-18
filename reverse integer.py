import sys
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
            return -self.reverse(-x)
        max_div_10 = (2**31-1)/10
        max_last_digit = (2**31-1)%10
        new = 0
        while x>0:
            digit = x % 10
            if (new > max_div_10) or (new == max_div_10 and digit > max_last_digit):
                return 0
            new = new * 10 + digit
            x = x / 10
        return new
            
sol = Solution()
print sol.reverse(1534236469)