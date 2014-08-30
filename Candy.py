class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        l = len(ratings)
        if l == 1:
            return 1
        elif l == 0:
            return 0
        candies = [1]*l
        while True:
            change = False
            for i in range(len(candies)):
                old_val = candies[i]
                if i == 0:
                    candies[i] = candies[i+1]+1 if ratings[i]>ratings[i+1] else candies[i]
                elif i == len(candies) -1:
                    candies[i] = candies[i-1]+1 if ratings[i]>ratings[i-1] else candies[i]
                else:
                    candies[i] = max((candies[i-1]+1 if ratings[i]>ratings[i-1] else candies[i]),(candies[i+1]+1 if ratings[i]>ratings[i+1] else candies[i]))
                if not old_val == candies[i]:
                    change = True
            if not change:
                break
        return sum(candies)
                
sol = Solution()

print sol.candy([0])