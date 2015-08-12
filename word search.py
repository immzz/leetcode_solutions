class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        visited = [[False for i in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.search(board,visited,word,0,i,j):
                    return True
        return False
    
    def search(self,board,visited,word,i,x,y):
        if not (board[x][y] == word[i]):
            return False
        elif i == len(word) - 1:
            return True
        
        visited[x][y] = True
         
        if x > 0 and (not visited[x-1][y]) and self.search(board,visited,word,i+1,x-1,y):
            return True
        if y > 0 and (not visited[x][y-1]) and self.search(board,visited,word,i+1,x,y-1):
            return True
        if x < len(board)-1 and (not visited[x+1][y]) and self.search(board,visited,word,i+1,x+1,y):
            return True
        if y < len(board[0])-1 and (not visited[x][y+1]) and self.search(board,visited,word,i+1,x,y+1):
            return True
            
        visited[x][y] = False
        return False

sol = Solution()
print sol.exist(["ab","cd"],"acdb")