class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_unique = 0 
        cur = 0

        while cur < len(nums):
            if nums[last_unique] == nums[cur]:
                cur += 1 

            else:
                last_unique += 1 
                nums[last_unique] = nums[cur]
                cur += 1 
        
        return last_unique + 1