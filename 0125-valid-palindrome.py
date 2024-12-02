class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if i.isdigit():
                new_s += str(i)
            elif i.isalpha():
                new_s += i.lower()
        
        print(new_s)
        if new_s[::-1] == new_s:
            return True 
        
        return False 
        