class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:

        total = sum(nums)
        outlier = -10**4

        nums_set = set(nums)
        nums = sorted(nums)

        for j in range(len(nums)):
            i = nums[j]
            if (j-1 >= 0 and nums[j-1] == i) or (j+1 < len(nums) and nums[j+1] == i):
                if (total - i) % 2 == 0 and (total - i) // 2 in nums_set:
                    outlier = max(outlier, i)
                
            else:
                nums_set.discard(i)
                if (total - i) % 2 == 0 and (total - i) // 2 in nums_set:
                    outlier = max(outlier, i)
                nums_set.add(i)

        
        return outlier
            

        