class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    
    # corner case: [2,3,4], 6 -> [1,3]
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l+1,r+1]

sol = Solution()
print sol.twoSum([2, 7, 11, 15],9)