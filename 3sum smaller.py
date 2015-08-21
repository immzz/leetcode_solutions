class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        count = 0
        for i in xrange(len(nums)-2):
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    count += r-l
                    l += 1
                else:
                    r -= 1
        return count
sol = Solution()
print sol.threeSumSmaller([], 0)