class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        from collections import defaultdict 
        d = defaultdict(set)
        min_length = 10**7

        for word in strs:
            if word == "":
                return ""
            min_length = min(min_length, len(word))
            for i in range(len(word)):
                d[i].add(word[i])
        
        ans = ""
        for j in range(min_length):
            if len(d[j]) == 1:
                ans += list(d[j])[0]
            else:
                break
        
        return ans 

