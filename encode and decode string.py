class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join([x.replace('|','||')+" | " for x in strs])
    
    # corner case: []
    # corner case: [""]
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = [x.replace('||','|') for x in s.split(' | ')]
        return res[:-1]

# Your Codec object will be instantiated and called as such:
codec = Codec()
print codec.encode([])
print codec.decode(codec.encode([]))