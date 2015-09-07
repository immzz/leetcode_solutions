class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        l,r = 0, len(height)-1
        total = 0
        min_height = 0
        while l < r:
            while l < r and height[l] <= min_height:
                total += min_height - height[l]
                l += 1
            while l < r and height[r] <= min_height:
                total += min_height - height[r]
                r -= 1
            min_height = min(height[l],height[r])
        return total