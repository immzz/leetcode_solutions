# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        candidate = 0
        for i in xrange(1,n):
            if not knows(i,candidate):
                candidate = i
        for i in xrange(n):
            if i == candidate:
                continue
            if (not knows(i,candidate)) or (knows(candidate,i)):
                return -1
        return candidate
        
 