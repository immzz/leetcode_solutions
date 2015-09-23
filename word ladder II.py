from sets import Set
class Solution(object):
    # corner case: "hot", "dog", ["hot","dog","cog","pot","dot"] -> [['hot', 'dot', 'dog']]
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        from collections import deque
        wordlist.add(endWord)
        wordlist.remove(beginWord)
        prev_dict = {beginWord:[]}
        current = [beginWord]
        res = []
        while len(wordlist) > 0 or endWord in current:
            #print wordlist
            if endWord in current:
                #print prev_dict
                self.getResult(prev_dict,endWord,deque(),res)
                return res
            new_reachable = {}
            for word in current:
                for i in xrange(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch != word[i] and word[:i]+ch+word[i+1:] in wordlist:
                            new_word = word[:i]+ch+word[i+1:]
                            if new_word in new_reachable:
                                new_reachable[new_word].append(word)
                            else:
                                new_reachable[new_word] = [word]
            #print new_reachable
            for new_word in new_reachable:
                wordlist.remove(new_word)
            prev_dict.update(new_reachable)
            current = new_reachable.keys()
            #print current,prev_dict
            if not current:
                break
        return res
                            
    def getResult(self,prev_dict,current_word,current_seq,res):
        current_seq.appendleft(current_word)
        if not prev_dict[current_word]:
            res.append(list(current_seq))
            current_seq.popleft()
            return
        for word in prev_dict[current_word]:
            self.getResult(prev_dict,word,current_seq,res)
        current_seq.popleft()
        
sol = Solution()
#{'hot': ['pot', 'dot'], 'pot': ['hot'], 'dot': ['hot'], 'dog': ['dot']}
print sol.findLadders("a","c", Set(["a","b",'c']))

