class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str1)):
            option = str1[:len(str1)-i]
            print(option)

            if not len(str1) % len(option) and option * (len(str1)//len(option)) == str1 and not len(str2) % len(option) and option * (len(str2) // len(option)) == str2:
                return option
        
        return ""

    
                
        