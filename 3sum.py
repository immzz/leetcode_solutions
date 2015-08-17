class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    
    # corner case: [-2,0,0,2,2] -> [[-2,0,2]]
    # corner case: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    # corner case: [-2,0,1,1,2] -> [[-2,0,2],[-2,1,1]]
    # corner case: [3,0,-2,-1,1,2] -> [[-2,-1,3],[-2,0,2],[-1,0,1]]
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[l]+nums[r]
                if s == -nums[i]:
                    res.append((nums[i],nums[l],nums[r]))
                    numl = nums[l]
                    while l < len(nums) and nums[l] == numl:
                        l += 1
                    numr = nums[r]
                    while r >=0 and nums[r] == numr:
                        r -= 1
                elif s < -nums[i]:
                    numl = nums[l]
                    while l < len(nums) and nums[l] == numl:
                        l += 1
                else:
                    numr = nums[r]
                    while r >=0 and nums[r] == numr:
                        r -= 1
            numi = nums[i]
            while i < len(nums) and nums[i] == numi:
                i += 1
        return res
                
                
                
            
            
            

sol = Solution()
print sol.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])