class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = [False,{}]

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.trie
        for c in word:
            if c not in current[1]:
                current[1][c] = [False,{}]
            current = current[1][c]
        current[0] = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.do_search(word,0,self.trie)
    def do_search(self,word,i,current):
        if not word:
            return True
        if i == len(word):
            return current[0]
        if word[i] == '.':
            for c in current[1]:
                if self.do_search(word,i+1,current[1][c]):
                    return True
            return False
        elif word[i] not in current[1]:
            return False
        else:
            return self.do_search(word,i+1,current[1][word[i]])

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")