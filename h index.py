class Solution(object):
    # corner case: [] -> 0
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        i = 0
        total = len(citations)-1
        while i < len(citations):
            if total-i+1 <= citations[i]:
                return total-i+1
            i += 1
        return 0