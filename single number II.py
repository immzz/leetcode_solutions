class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b = 0,0
        for i in xrange(len(nums)):
            c = nums[i]
            na = (a&~b&~c)|(~a&b&c)
            nb = (~a&b&~c)|(~a&~b&c)
            a,b = na,nb
        return ~a&b