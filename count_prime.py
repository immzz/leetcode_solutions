class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        is_prime = [False,False]+([True] * (n-2))
        for i in range(2,n):
            if is_prime[i]:
                j = i*2
                while j < n:
                    is_prime[j] = False
                    j += i
        return sum(is_prime)

sol = Solution()
print sol.countPrimes(5)
                