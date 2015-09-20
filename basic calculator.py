class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '('+s+')'
        i = 0
        current_num = 0
        arr = []
        while i < len(s):
            #print arr
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '+' or s[i] == '-' or s[i] == '(':
                arr.append(s[i])
                i += 1
                continue
            if s[i] == ')':
                prev = arr.pop()
                op = None
                sum_num = None
                current_num = None
                while prev != '(':
                    if prev == '-':
                        sum_num -= current_num*2
                    elif prev != '+':
                        current_num = prev
                        if sum_num is not None:
                            sum_num += current_num
                        else:
                            sum_num = current_num
                        
                    prev = arr.pop()
                if sum_num is not None:
                    arr.append(sum_num)
                i += 1
                continue
            
            if s[i].isdigit():
                current_num = 0
                while s[i].isdigit() and i < len(s):
                    current_num = current_num * 10 + int(s[i])
                    i += 1
                arr.append(current_num)
        return 0 if not arr else arr[0]

sol = Solution()
print sol.calculate(" 2-1 + 2 ")
        
                        
        