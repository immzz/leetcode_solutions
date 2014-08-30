class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        
        visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]  
        current_dire = 'right'
        x = 0;
        y = 0;
        
        
        result = []
        
        
        
        while True:
            result = result + [matrix[x][y]]
            visited[x][y] = True
            if current_dire == 'right':
                #try right
                if y + 1 < len(matrix[0]) and not visited[x][y+1]:
                    y = y + 1
                elif x + 1 < len(matrix) and not visited[x+1][y]:
                    current_dire = 'down'
                    x = x + 1
                else:
                    break
            elif current_dire == 'down':
              #try down
              if x + 1 < len(matrix) and not visited[x+1][y]:
                  x = x + 1
              elif y - 1 >= 0 and not visited[x][y-1]:
                  current_dire = 'left'
                  y = y - 1
              else:
                  break
            elif current_dire == 'left':
              #try left
              if y - 1 >= 0 and not visited[x][y-1]:
                  y = y - 1
              elif x - 1 >= 0 and not visited[x-1][y]:
                  current_dire = 'up'
                  x = x - 1
              else:
                  break 
            elif current_dire == 'up':
              #try up
              if x - 1 >= 0 and not visited[x-1][y]:
                  x = x - 1
              elif y + 1 < len(matrix[0]) and not visited[x][y+1]:
                  current_dire = 'right'
                  y = y + 1
              else:
                  break
        return result
        
sol = Solution()
print sol.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
              
            