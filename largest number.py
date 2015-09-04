class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str,nums)
        nums.sort(cmp = lambda a,b:cmp(a+b,b+a),reverse=True)
        return str(int("".join(nums)))

sol = Solution()
print sol.largestNumber([3,30,34,5,9])