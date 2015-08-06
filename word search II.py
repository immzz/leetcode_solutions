class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        trie = self.buildTrie(words)
        #print trie
        visited = [[False] * len(board[0]) for x in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.search(board,trie,i,j,visited)
        #print trie
        res = []
        word = []
        self.getResult(trie,res,word)
        return res
        
    def search(self,board,trie_node,x,y,visited):
        if board[x][y] not in trie_node[1]:
            return
        trie_node = trie_node[1][board[x][y]]
        #print x,y
        if trie_node[0]:
            trie_node[2] = True
        
        visited[x][y] = True
        if x > 0 and (not visited[x-1][y]):
            self.search(board,trie_node,x-1,y,visited)
        if y > 0 and (not visited[x][y-1]):
            self.search(board,trie_node,x,y-1,visited)
        if (x < len(board) - 1) and (not visited[x+1][y]):
            self.search(board,trie_node,x+1,y,visited)
        if (y < len(board[0]) - 1) and (not visited[x][y+1]):
            self.search(board,trie_node,x,y+1,visited)
        visited[x][y] = False
            
    def buildTrie(self,words):
        trie = [False,{},False] #is word,next,is in dict
        for word in words:
            current = trie
            for c in word:
                if c not in current[1]:
                    current[1][c] = [False,{},False]
                current = current[1][c]
            current[0] = True
        return trie
    
    def getResult(self,trie,res,word):
        if trie[2]:
            res.append("".join(word))
        for k in trie[1]:
            word.append(k)
            self.getResult(trie[1][k],res,word)
            del word[-1]

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
sol = Solution()
print sol.findWords(board,words)
    
                    