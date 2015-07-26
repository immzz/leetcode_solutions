class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k = (k % len(nums)) if (k >= len(nums)) else k
        if not k == 0:
            nums[:] = nums[-k:] + nums[:(len(nums)-k)]
        
sol = Solution()
a = [1,2]
sol.rotate(a,2)
print a