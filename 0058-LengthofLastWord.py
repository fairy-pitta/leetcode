class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = list(s.split(" "))

        while True:
            for i in reversed(li):
                if len(i) > 0:
                    return len(i)
                    
