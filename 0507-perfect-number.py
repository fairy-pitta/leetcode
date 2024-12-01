class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        divisor_sum = 0 


        for i in range(2, int(num**0.5)+1):
            if not num % i:
                divisor_sum += i
                divisor_sum += num // i
        
        if num > 1:
            divisor_sum += 1 
            
        if num == divisor_sum:
            return True 
        else:
            return False