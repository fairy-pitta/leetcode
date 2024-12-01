class Solution:
    def fib(self, n: int) -> int:
        bef = 1
        cur = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1 
        else:
            for i in range(n-2):
                temp = cur 
                cur = cur + bef 
                bef = temp 
            
            return cur