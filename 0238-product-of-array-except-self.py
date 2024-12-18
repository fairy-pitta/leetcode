class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accum = [(1) for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            accum[i] = accum[i-1] * nums[i-1]
        
        ans = [(1) for _ in range(len(nums))]
        suffix = 1

        for j in reversed(range(len(nums))):
            ans[j] = suffix * accum[j]
            suffix *= nums[j]
        
        return ans
