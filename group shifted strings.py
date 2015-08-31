class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            if not s:
                dic[[]] = {""}
                continue
            transform = ['a']*len(s)
            for i in xrange(1,len(s)):
                offset = ord(s[i]) - ord(s[0])
                if offset < 0:
                    offset += 26
                transform[i] = chr(offset+ord('a'))
            transform_str = "".join(transform)
            if transform_str in dic:
                dic[transform_str].append(s)
            else:
                dic[transform_str] = [s]
        return [sorted(x) for x in dic.values()]
            

sol = Solution()
print sol.groupStrings(["a","b"])
