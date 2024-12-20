class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()

        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.discard(i)
        
        return list(s)[0]