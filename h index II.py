class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        total = len(citations)-1
        for i in xrange(len(citations)):
            if total - i + 1 <= citations[i]:
                return total-i+1
        return 0