from sets import Set
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        from sets import Set
        wordDict.add(endWord)
        
        count = 1
        
        current = Set([beginWord])
        while len(current) > 0:
            if endWord in current:
                return count
            new_reachable = Set([])
            
            for word in current:
                for i in xrange(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch != word[i] and (word[:i]+ch+word[i+1:]) in wordDict:
                            wordDict.remove(word[:i]+ch+word[i+1:]) 
                            new_reachable.add(word[:i]+ch+word[i+1:])
            current = new_reachable
            #print current
            count += 1
        return 0
    def oneCharacterDifferent(self,word1,word2):
        if len(word1) != len(word2):
            return False
        i = 0
        while i < len(word1) and word1[i] == word2[i]:
            i += 1
        if i == len(word1):
            return False
        i += 1
        while i < len(word1):
            if word1[i] != word2[i]:
                return False
            i += 1
        return True

sol = Solution()
print sol.ladderLength("hit","cog",Set(["hot","dot","dog","lot","log"]))