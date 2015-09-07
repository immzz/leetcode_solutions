class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from sets import Set
        s = Set(nums)
        res = 0
        for n in nums:
            if (n-1) not in s:
                m = n+1
                current = 1
                while m in s:
                    current += 1
                    m += 1
                res = max(res,current)
        return res