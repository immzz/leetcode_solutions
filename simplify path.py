class Solution:
    # @param {string} path
    # @return {string}
    
    # corner case: "/" -> "/"
    def simplifyPath(self, path):
        real_path = ["",]
        start = 0
        for i in xrange(len(path)):
            if path[i] == '/':
                if i>start:
                    current = path[start:i]
                    if current == '..':
                        if len(real_path) > 1:
                            real_path.pop()
                    elif current != '.':
                        real_path.append(current)
                start = i+1
        if start < len(path):
            current = path[start:]
            if current == '..':
                if len(real_path) > 1:
                    real_path.pop()
                else:
                    return "/"
            elif current != '.':
                real_path.append(current)
        return "/".join(real_path) if len(real_path) > 1 else "/"

sol = Solution()
print sol.simplifyPath('/./..')