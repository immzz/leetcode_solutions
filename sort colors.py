class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        red_ptr = -1
        blue_ptr = len(nums)
        i = 0
        while i < blue_ptr and i < len(nums) and red_ptr < len(nums):
            print i
            if nums[i] == 0:
                red_ptr += 1
                nums[i] = nums[red_ptr]
                nums[red_ptr] = 0
                i += 1
            elif nums[i] == 2:
                blue_ptr -= 1
                nums[i] = nums[blue_ptr]
                nums[blue_ptr] = 2
            else:
                i += 1
            
        
sol = Solution()
a = [1,2,0]
sol.sortColors(a)
print a