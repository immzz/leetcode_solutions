class Solution:
    # @param {string} str
    # @return {integer}
    
    # corner case: '+1' -> 1
    # corner case: '+-2' -> 0
    # corner case: "     +004500" -> 4500
    # corner case: "  -0012a42" -> -12
    # corner case: "-2147483648" -> -2147483648
    # corner case: "2147483648" -> 2147483647
    def myAtoi(self, str):
        if not str:
            return 0
        multiplier = 1
        i = 0
        while str[i] == ' ':
            i += 1
        sign_count = 0
        while str[i] == '+' or str[i] == '-':
            if sign_count > 0:
                return 0
            sign_count += 1
            if str[i] == '-':
                multiplier = -1
            i += 1
        if str[i] == ' ':
            return 0
        max_div_10 = (2**31-1)/10
        max_last_digit = (2**31-1)%10
        #print max_last_digit
        num = 0
        while i < len(str):
            try:
                digit = int(str[i])
            except:
                break
            if (multiplier == 1) and ((num > max_div_10) or (num == max_div_10 and digit > max_last_digit)):
                return 2**31 - 1
            if (multiplier == -1) and ((num > max_div_10) or (num == max_div_10 and digit > max_last_digit+1)):
                #print "OKO"
                return -2**31
            num = num * 10 + digit
            #print num
            i += 1
        return num*multiplier
            
            
sol = Solution()
print sol.myAtoi("-2147483648")