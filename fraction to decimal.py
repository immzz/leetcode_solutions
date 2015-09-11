class Solution(object):
    # corner case: -2147483648, 1 -> -2147483648
    # corner case: 7,-12 -> 0.58(3)
    # corner case: 0,-5 -> 0
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = '-' if ((numerator < 0) ^ (denominator < 0)) else ''
        head,remainder = divmod(abs(numerator),abs(denominator))
        res += str(head)
        if not remainder:
            return res if head else "0"
        res += '.'
        d = {remainder:len(res)}
        while remainder:
            
            digit,remainder = divmod(remainder * 10,abs(denominator))
            #print remainder,d
            res += str(digit)
            
            #print remainder,d
            if remainder in d:
                return res[:(d[remainder])]+'('+res[d[remainder]:]+')'
            d[remainder] = len(res)
        return res
            
sol = Solution()
print sol.fractionToDecimal(0, -5)