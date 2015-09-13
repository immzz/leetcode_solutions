class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current_min = nums[0]
        current_max = nums[0]
        res = nums[0]
        for num in nums[1:]:
            current_max,current_min = max(num,current_max*num,current_min*num),min(num,current_max*num,current_min*num)
            res = max(res,current_max)
        return res

sol = Solution()
print sol.maxProduct([-4,-3,-2])