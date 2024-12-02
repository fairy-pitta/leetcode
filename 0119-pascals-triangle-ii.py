class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
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
        
        ans = []
        for i in range(rowIndex+1):
            ans.append(comb(rowIndex, i))
            
        
        return ans
