class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if not nums:
            return 0
        start = 0
        current_step = 0
        current_reachable = 0
        while True:
            if current_reachable >= len(nums)-1:
                return current_step
            current_step += 1
            next_reachable = 0
            while start <= current_reachable:
                next_reachable = max(next_reachable,nums[start]+start)
                start += 1
            start,current_reachable = current_reachable+1,next_reachable
        return current_step

sol = Solution()
print sol.jump([2,3,1,1,4])