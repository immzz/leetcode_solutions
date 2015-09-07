class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in xrange(len(board)):
            if board[i][0] == 'O':
                self.solveDo(board,i,0)
            if board[i][len(board[0])-1] == 'O':
                self.solveDo(board,i,len(board[0])-1)
        for j in xrange(len(board[0])):
            if board[0][j] == 'O':
                self.solveDo(board,0,j)
            if board[len(board)-1][j] == 'O':
                self.solveDo(board,len(board)-1,j)
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
                
    def solveDo(self,board,i,j):
        from Queue import Queue
        q = Queue()
        q.put((i,j))
        #print "ENter"
        while q.qsize():
            #print q.qsize()
            p = q.get()
            #sprint p
            i,j = p[0],p[1]
            #print i,j,board[i][j]
            if board[i][j] != 'O':
                continue
            #print "OK"
            board[p[0]][p[1]] = 'M'
            if i > 0 and board[i-1][j] == 'O':
                q.put((i-1,j))
            if j > 0 and board[i][j-1] == 'O':
                q.put((i,j-1))
            if i < len(board)-1 and board[i+1][j] == 'O':
                q.put((i+1,j))
            if j < len(board[0])-1 and board[i][j+1] == 'O':
                q.put((i,j+1))

sol = Solution()
a = [list("OOO"),list("OOO"),list("OOO")]
sol.solve(a)
print a