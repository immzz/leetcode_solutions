class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:
            return True
        reachable = 0
        for i in xrange(len(nums)):
            if i <= reachable:
                reachable = max(reachable,nums[i]+i)
        return reachable >= len(nums)-1

sol = Solution()

print sol.canJump([0,1])