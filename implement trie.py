class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isEnd = False
        self.next = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for c in word:
            if not c in current.next:
                current.next[c] = TrieNode()
            current = current.next[c]
        current.isEnd = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for c in word:
            if not c in current.next:
                return False
            current = current.next[c]
        return current.isEnd

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if not c in current.next:
                return False
            current = current.next[c]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")