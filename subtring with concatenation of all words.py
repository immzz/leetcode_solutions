class Solution(object):
    # corner case: "wordgoodgoodgoodbestword", ["word","good","best","good"] -> [8]
    # corner case: "aaaaaaaa", ["aa","aa","aa"] -> [0,1,2]
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        l = len(words[0])
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        count_dic = {}
        for word in dic:
            count_dic[word] = dic[word]
        i,j = 0,0
        res = []
        while i < len(s):
            #print i,j
            j = i
            current_count = 0
            while j+l <= len(s):
                sub = s[j:j+l]
                if sub in dic and count_dic[sub] > 0:
                    j += l
                    count_dic[sub] -= 1
                    current_count += 1
                else:
                    break
            if current_count == len(words):
                res.append(i)
            i += 1
            for k in count_dic:
                count_dic[k] = dic[k]
        return res

sol = Solution()
print sol.findSubstring("aaaaaaaa", ["aa","aa","aa"])






