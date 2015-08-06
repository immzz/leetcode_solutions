class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                return True
            dict[num] = True
        return False