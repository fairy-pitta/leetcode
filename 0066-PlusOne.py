class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        for i in digits:
            str_digits += str(i)
        large_int = int(str_digits)
        new_int = large_int + 1 
        ans = []
        for j in str(new_int):
            ans.append(int(j))
        return ans
        