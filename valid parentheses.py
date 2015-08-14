class Solution:
    # @param {string} s
    # @return {boolean}
    # corner case: "[" -> false
    # corner case: "[(])" -> false
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if len(stack) > 0:
                    prev = stack.pop()
                    if not ((prev == '(' and c == ')') or (prev == '{' and c == '}') or (prev == '[' and c == ']')):
                        return False
                else:
                    return False
        return len(stack) == 0

sol = Solution()
print sol.isValid('([)]')