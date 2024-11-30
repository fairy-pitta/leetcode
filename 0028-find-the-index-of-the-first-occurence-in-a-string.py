class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1 

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                flag = True
                for j in range(len(needle)):
                    if i+j >= len(haystack):
                        flag = False
                    elif haystack[i+j] != needle[j]:
                        flag = False
                
                if flag:
                    ans = i
                    return ans 
                else:
                    continue
        
        return ans
        