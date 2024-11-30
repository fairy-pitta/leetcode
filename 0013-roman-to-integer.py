class Solution:
    def romanToInt(self, s: str) -> int:

        ans = 0
        counted= False
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(len(s)):
            if i == len(s)-1:
                if not counted:
                    ans += d[s[i]]
            elif counted:
                counted = False
                continue
            elif d[s[i]] >= d[s[i+1]]:
                ans += d[s[i]]
                counted = False
            else:
                ans += d[s[i+1]] - d[s[i]]
                counted = True
        
        return ans