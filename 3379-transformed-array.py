class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [(0) for _ in range(len(nums))]

        for i in range(len(nums)):
            if nums[i] > 0:
                idx = (i + nums[i]) % len(nums)
                result[i] = nums[idx]
            elif nums[i] < 0:
                idx = (i - abs(nums[i])) % len(nums)
                result[i] = nums[idx]
            else:
                result[i] = nums[i]

        return result