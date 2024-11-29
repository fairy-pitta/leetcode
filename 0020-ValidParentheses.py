class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque 

        d = deque()

        for bracket in list(s):
            if bracket == "(" or bracket == "{" or bracket == "[":
                d.append(bracket)
            elif d and bracket == ")":
                pair = d.pop()
                if pair != "(":
                    return False 
            elif d and bracket == "}":
                pair = d.pop()
                if pair != "{":
                    return False 
            elif d and bracket == "]":
                pair = d.pop()
                if pair != "[":
                    return False
            else:
                return False
            
        if d:
            return False 
        else:
            return True

        