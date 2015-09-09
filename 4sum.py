class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        #print nums
        res = []
        i,j = 0,1
        while i < len(nums)-3:
            j = i+1
            while j < len(nums)-2:
                l = j+1
                r = len(nums)-1
                part1 = nums[i]+nums[j]
                while l < r:
                    s = part1+nums[l]+nums[r]
                    if s < target:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s == target:
                        res.append((nums[i],nums[j],nums[l],nums[r]))
                        #print i,j,l,r
                        #print (nums[i],nums[j],nums[l],nums[r])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                j += 1
                while j < len(nums)-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < len(nums)-3 and nums[i] == nums[i-1]:
                i += 1
        return res
                    
                            
sol = Solution()
print sol.fourSum([1,0,-1,0,-2,2],0)