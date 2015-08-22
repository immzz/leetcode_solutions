class Solution(object):
    # corner case: [],1,1
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            r = self.generateRange(lower,upper)
            return [r] if r else []
        res = []
        if nums[0] > lower:
            res.append(self.generateRange(lower,nums[0]-1))
        for i in xrange(1,len(nums)):
            r = self.generateRange(nums[i-1]+1,nums[i]-1)
            if r:
                res.append(r)
        r = self.generateRange(nums[-1]+1,upper)
        if r:
            res.append(r)
        return res
            
    def generateRange(self,start,end):
        if start == end:
            return str(start)
        elif start < end:
            return str(start)+'->'+str(end)
            
sol = Solution()
print sol.findMissingRanges([2],1,3)