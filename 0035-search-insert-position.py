class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left 
        idx = bisect_left(nums, target)
        return idx