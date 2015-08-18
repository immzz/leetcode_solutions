class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        filled_single = [0] * 9
        for i in (0,3,6):
            for j in (0,3,6):
                if not self.checkSquare(board,i,j,filled_single):
                    return False
        for i in xrange(9):
            if not self.checkLine(board,i,filled_single):
                return False
        return True

    def checkSquare(self,nums,top,left,filled_single):
        filled_single = [0] * 9
        for i in xrange(top,top+3):
            for j in xrange(left,left+3):
                v = nums[i][j]
                if v != '.':
                    filled_single[int(v)-1] += 1
        return sum([x<=1 for x in filled_single]) == 9
    def checkLine(self,nums,i,filled_single):
        filled_single = [0] * 9
        for j in xrange(9):
                v = nums[i][j]
                if v != '.':
                    filled_single[int(v)-1] += 1
        if not sum([x<=1 for x in filled_single]) == 9:
            return False
        filled_single = [0] * 9
        for j in xrange(9):
                v = nums[j][i]
                if v != '.':
                    filled_single[int(v)-1] += 1
        if not sum([x<=1 for x in filled_single]) == 9:
            return False
        return True
        
   
a = ["..4...63."
,"........."
,"5......9."
,"...56...."
,"4.3.....1"
,"...7....."
,"...5....."
,"........."
,"........."]
sol = Solution()
print sol.isValidSudoku(a)