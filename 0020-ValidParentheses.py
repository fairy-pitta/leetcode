class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == "(" and s[j] == ")":
                    s[i] = ""
                    s[j] = ""
                elif s[i] == "{" and s[j] == "}":
                    s[i] = ""
                    s[j] = ""
                elif s[i] == "[" and s[j] == "]":
                    s[i] = ""
                    s[j] = ""
        
        if "".join(s) == '':
            return True
        else:
            return False