class Solution(object):
    # corner case: "0","0" -> "0"
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        s = [0]* (len(num1)+len(num2)+1)
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                s[i+j] += int(num1[i])*int(num2[j])
        new_s = []
        carry = 0
        for i in xrange(len(s)):
            sum = s[i] + carry
            s[i] = sum % 10
            carry = sum/10
        i = len(s)-1
        while i>=0 and s[i] == 0:
            i -= 1
        while i >= 0:
            new_s.append(str(s[i]))
            i -= 1
        return "".join(new_s) if new_s else "0"
        
        
        
sol = Solution()
print sol.multiply("123","11")