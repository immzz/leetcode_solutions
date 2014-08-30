class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        res = ''
        direction = 'down' # or 'up'
        for row in range(nRows):
            height = nRows - row
            index = row
            direction = 'down'
            while index < len(s):
                if direction == 'down' and row == nRows -1:
                    direction = 'up'
                    continue
                elif direction == 'up' and row == 0:
                    direction = 'down'
                    continue
                res += s[index] 
                if direction == 'down':
                    index += (height - 1) * 2
                    direction = 'up'
                elif direction == 'up':
                    index += 2 * row
                    direction = 'down'
        return res
        
sol = Solution()
print sol.convert("ABCD", 4)
                    