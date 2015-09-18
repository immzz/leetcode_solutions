class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r,b = 0,len(nums)-1
        i = 0
        while i <= b:
            while i >= r and i <= b and nums[i] != 1:
                if nums[i] == 0:
                    nums[i] = nums[r]
                    nums[r] = 0
                    r += 1
                elif nums[i] == 2:
                    nums[i] = nums[b]
                    nums[b] = 2
                    b -= 1
            i += 1
                    
            
        
sol = Solution()
a = [1,2,0]
sol.sortColors(a)
print a