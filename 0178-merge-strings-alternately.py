class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        from collections import deque
        word1_deque = deque(list(word1))
        word2_deque = deque(list(word2))
        ans = ""
        while word1_deque and word2_deque:
            ans += word1_deque.popleft()
            ans += word2_deque.popleft()
        
        if word1_deque:
            ans += "".join(list(word1_deque))
        elif word2_deque:
            ans += "".join(list(word2_deque))
        
        return ans


        