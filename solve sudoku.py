class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = [[False for i in xrange(9)] for j in xrange(9)]
        missing = [[[True for k in xrange(9)] for i in xrange(9)] for j in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    self.solveDo(board,visited,missing,i,j)
                    
        
    def solveDo(self,board,visited,missing,i,j):
        if board[i][j] != '.':
            return
        visited[i][j] = True
        self.update(board,missing,i,j)
        #print missing[i][j]
        print i,j
        if sum(missing[i][j]) == 1:
            board[i][j] = str(missing[i][j].index(False)+1)
            print 'filled',i,j,board[i][j]
        else:
            #print visited
            for k in xrange(9):
                if board[i][k] == '.' and not visited[i][k]:
                    self.solveDo(board,visited,missing,i,k)
                    self.update(board,missing,i,j)
                    if sum(missing[i][j]) == 1:
                        board[i][j] = str(missing[i][j].index(False)+1)
                if board[k][j] == '.' and not visited[k][j]:
                    self.solveDo(board,visited,missing,k,j)
                    self.update(board,missing,i,j)
                    if sum(missing[i][j]) == 1:
                        board[i][j] = str(missing[i][j].index(False)+1)
            topi,topj = (i/3)*3,(j/3)*3
            for k1 in xrange(3):
                for k2 in xrange(3):
                    if board[k1+topi][k2+topj] == '.' and not visited[k1+topi][k2+topj]:
                        self.solveDo(board,visited,missing,k1+topi,k2+topj)
                        self.update(board,missing,i,j)
                        if sum(missing[i][j]) == 1:
                            board[i][j] = str(missing[i][j].index(False)+1)
        visited[i][j] = False
    def update(self,board,missing,i,j):    
        for k in xrange(9):
            if board[i][k] != '.':
                #print board[i][k],ord(board[i][k])-ord('1')
                missing[i][j][ord(board[i][k])-ord('1')] = False
            if board[k][j] != '.':
                #print board[k][j],ord(board[k][j])-ord('1')
                missing[i][j][ord(board[k][j])-ord('1')] = False
        
        topi,topj = (i/3)*3,(j/3)*3
        for k1 in xrange(3):
            for k2 in xrange(3):
                if board[k1+topi][k2+topj] != '.':
                    missing[i][j][ord(board[k1+topi][k2+topj])-ord('1')] = False

sol = Solution()
a = \
["..9748..."
,"7........"
,".2.1.9..."
,"..7...24."
,".64.1.59."
,".98...3.."
,"...8.3.2."
,"........6"
,"...2759.."]
a = [list(x) for x in a]
print a
sol.solveSudoku(a)
print a