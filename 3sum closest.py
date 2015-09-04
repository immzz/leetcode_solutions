import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best_diff = sys.maxint
        best_sum = 0
        for i in xrange(len(nums)-2):
            s = nums[i] + nums[i+1] + nums[len(nums)-1]
            diff = abs(s - target)
            l = i+1
            r = len(nums)-1
            while l+1 < r:
                diff_l = abs(nums[i] + nums[l+1] + nums[r] - target)
                diff_r = abs(nums[i] + nums[l] + nums[r-1] - target)
                if diff_l <= diff and diff_l < diff_r:
                    diff = diff_l
                    s = nums[i] + nums[l+1] + nums[r]
                    l += 1
                elif diff_r <= diff:
                    diff = diff_r
                    s = nums[i] + nums[l] + nums[r-1]
                    r -= 1
                else:
                    break
            if best_diff > diff:
                best_diff = diff
                best_sum = s
        return best_sum

sol = Solution()
print sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)