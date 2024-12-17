class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        ans = []

        for i in range(len(candies)):
            if candies[i] == max_num:
                ans.append(True)
            elif candies[i] + extraCandies >= max_num:
                ans.append(True)
            else:
                ans.append(False)
            
        return ans
        