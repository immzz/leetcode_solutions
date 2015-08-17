import sys
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        pos1 = -1
        pos2 = -1
        min = sys.maxint
        for i in xrange(len(words)):
            if words[i] == word1:
                pos1 = i
            elif words[i] == word2:
                pos2 = i
            if (pos1>=0) and (pos2>=0) and (abs(pos1-pos2) < min):
                min = abs(pos1-pos2)
        return min

sol = Solution()
print sol.shortestDistance(["a","b"], "a", "b")