class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0
        prev_high_index = 0
        bottom = 0
        total = 0
        i = 1
        while i < len(height):
            if height[i] < height[i-1]:
                total += min(height[prev_high_index],height[i-1])*(i-1-prev_high_index)-bottom
                prev_high_index = i-1
                bottom = height[i]
            else:
                bottom += min(height[i],height[prev_high_index])
            print i,total,bottom
            i += 1
        total += min(height[prev_high_index],height[i-1])*(i-1-prev_high_index)-bottom
        return total

sol = Solution()
print sol.trap([2,1,0,2])