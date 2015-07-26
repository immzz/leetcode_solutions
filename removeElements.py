class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if (not nums) or len(nums) < 1:
            return 0
        length = len(nums)
        val_ptr = 0
        current_ptr = 0
        while (val_ptr < len(nums)) and (current_ptr < len(nums)):
            while (val_ptr < len(nums)) and (not (nums[val_ptr] == val)):
                val_ptr += 1
            current_ptr = val_ptr + 1
            while (current_ptr < len(nums)) and (nums[current_ptr] == val):
                current_ptr += 1
            if (current_ptr < len(nums)) and (val_ptr < len(nums)):
                temp = nums[current_ptr]
                nums[current_ptr] = nums[val_ptr]
                nums[val_ptr] = temp
                val_ptr += 1
                current_ptr += 1
        return val_ptr

sol = Solution()
a = [2,3,3]
print sol.removeElement(a,2)
print a