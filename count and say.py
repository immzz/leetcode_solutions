class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        s = [1]
        
        while n > 1:
            new_s = []
            count = 1
            prev = s[0]
            for i in xrange(1,len(s)):
                if s[i] != prev:
                    new_s.append(count)
                    new_s.append(prev)
                    prev = s[i]
                    count = 1
                else:
                    count += 1
            new_s.append(count)
            new_s.append(prev)
            s = new_s[:]
            n -= 1
        return "".join([str(x) for x in s])

sol = Solution()
print sol.countAndSay(20)