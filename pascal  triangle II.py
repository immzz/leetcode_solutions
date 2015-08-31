class Solution(object):
    # corner case: 0 -> []
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        current_row = [1]*(rowIndex+1)
        next_row = [1]*(rowIndex+1)
        for i in xrange(2,rowIndex+1):
            for j in xrange(1,i):
                next_row[j] = current_row[j-1] + current_row[j]
            next_row[i] = 1
            current_row = next_row[:]
        return current_row
        