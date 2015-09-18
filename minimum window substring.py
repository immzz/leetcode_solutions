class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        count_dict = {}
        for c in t:
            if c not in count_dict:
                count_dict[c] = 1
            else:
                count_dict[c] += 1
        run_dict = {}
        for c in count_dict:
            run_dict[c] = 0
        remaining = len(t)
        start,end = 0,0
        min_str = ""
        min_len = sys.maxint
        while end < len(s):
            if s[end] not in count_dict:
                end += 1
                continue
            run_dict[s[end]] += 1
            if run_dict[s[end]] <= count_dict[s[end]]:
                remaining -= 1
            if remaining == 0:
                while start <= end and remaining == 0:
                    if s[start] not in count_dict:
                        start += 1
                        continue
                    run_dict[s[start]] -= 1
                    if run_dict[s[start]] < count_dict[s[start]]:
                        remaining += 1
                        if end - start + 1 < min_len:
                            min_len = end-start+1
                            min_str = s[start:end+1]
                    start += 1
            end += 1
        return min_str
                    
                
            
            