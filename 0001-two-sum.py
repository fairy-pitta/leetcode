from collections import defaultdict 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        s = set()
        ans = []

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in s:
                ans = [i,d[pair][0]]
            else:
                s.add(nums[i])
                d[nums[i]].append(i)
        return ans 
    

