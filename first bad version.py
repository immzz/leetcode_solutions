# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.firstBadVersionDo(1,n)
    def firstBadVersionDo(self,l,r):
        if l == r:
            return l
        m = (l+r)/2
        if isBadVersion(m):
            return self.firstBadVersionDo(l,m)
        else:
            return self.firstBadVersionDo(m+1,r)
        