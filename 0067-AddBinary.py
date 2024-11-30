class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ten = int(a, 2)
        b_ten= int(b, 2)
        return format(a_ten+b_ten, 'b')