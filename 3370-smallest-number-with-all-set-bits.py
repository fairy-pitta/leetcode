class Solution:
    def smallestNumber(self, n: int) -> int:

        power = 0
        while True:
            if 2 ** power - 1 >= n:
                return 2 ** power - 1
            
            power += 1 
