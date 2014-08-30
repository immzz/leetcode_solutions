class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dic):
        lst = []
        self.search(s,0,dic,'',lst)
        return lst
    def search(self,s,start_index,dic,sentence,sentences):
        if start_index == len(s):
            sentences.append(sentence)
        for word in dic:
            if s.find(word,start_index,start_index+len(word)) == start_index:
                
                self.search(s,start_index+len(word),dic,word if sentence == '' else sentence+' '+word,sentences)

sol = Solution()
print sol.wordBreak('catsanddog',["cat", "cats", "and", "sand", "dog"])