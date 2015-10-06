class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from sets import Set
        res = Set([])
        num_set = Set([])
        if len(s) <= 10:
            return []
        current = 0
        for i in xrange(10):
            current = (((current << 2) | self.charToDigit(s[i])) & 0xfffff)
        num_set.add(current)
        for i in xrange(10,len(s)):
            current = ((current << 2) | self.charToDigit(s[i])) & 0xfffff
            if current in num_set:
                res.add(s[i-9:i+1])
            else:
                num_set.add(current)
        return list(res)
        
        
    def charToDigit(self,c):
        if c == 'A':
            return 0
        elif c == 'T':
            return 1
        elif c == 'C':
            return 2
        else:
            return 3
        
["GTTCTCACTA","TGGGTTCTCA","GGTGTTTTCG","TCCGCTTTCC","CTTGCGAGAC","CCGCTTTCCT","TGACTGCGTG","GCTCCGCTTT","GACTGCGTGG"]
"CGACGCAATTTAGAACGGGCCGCACTGCAACCATTGCTCAGACAACGCATGAGTTAAATTTCACAAGTGATAGTGGCTTGCGAGACGTGGGTTGGTGGTAGCGTACGCCCGCTATTCGCCCCTAACGTGACGGGATTATAAGGTCGCTTCCCGGAATGCGCAGACGAGTCTCCGGTTTAGCCTAGACGTCTCACGCGCGCAAGGCGTCAGTTCTCACTATCTCGCACAGGTGTATTCTATTAGTTATGGGTTCTCACTACAGTCGGTTACTTCCTCATCCATTTCTGCATACGGGTCAACTAACAGTGTCATGGGGTATTGGGAAGGATGCGTTTTTAAACCCTCTCAGTAGCGCGAGGATGCCCACAAATACGACGGCGGCCACGGATCTAATGCGAAGCTAGCGACGCTTTCCAGCAACGAGCGCCCCACTTATGACTGCGTGGGGCGCTCCGCTTTCCTAGAGAACATAGATGGTGTTTTCGAATCGTAACCACTTA"