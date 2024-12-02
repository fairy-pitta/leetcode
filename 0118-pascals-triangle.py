class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def comb(n, k):
            from math import factorial

            if n == 0 and k == 0:
                return 1

            if n == 0:
                return 0
            
            if k == 0:
                return 1
            
            if n == k:
                return 1
            
            return factorial(n) // (factorial(k) * factorial(n-k))
        
        ans = [[] for _ in range(numRows)]
        for row in range(numRows):
            for col in range(row+1):
                ans[row].append(comb(row, col))
            
        
        return ans