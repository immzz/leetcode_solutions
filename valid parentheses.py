class Solution:
    # @param {string} s
    # @return {boolean}
    # corner case: "[" -> false
    # corner case: "[(])" -> false
    def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            stack = []
            d = {')':'(',']':'[','}':'{'}
            for c in s:
                if c in '([{':
                    stack.append(c)
                else:
                    if not stack or stack.pop() != d[c]:
                        return False
            return len(stack) == 0

sol = Solution()
print sol.isValid('([)]')