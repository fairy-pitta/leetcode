# 0643 Maximum Average Subarray I

## Problem URL

[https://leetcode.com/problems/maximum-average-subarray-i/](https://leetcode.com/problems/maximum-average-subarray-i/)

## Problem Overview

Given an integer array `nums` consisting of `n` elements, and an integer `k`, find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. 

Any answer with a calculation error less than `10⁻⁵` will be accepted.

### Example 1:
**Input:**  
`nums = [1,12,-5,-6,50,3]`, `k = 4`  
**Output:**  
`12.75000`  
**Explanation:**  
Maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`

### Example 2:
**Input:**  
`nums = [5]`, `k = 1`  
**Output:**  
`5.00000`  

## Constraints:
- `n == nums.length`
- `1 <= k <= n <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`


## Solution 

The brutal solution would compute all the possible average by running two forloops nested in one another, but that would be computationally too complex (`O(n*k)`). 
Hence I took a different approach here. 

Note that when we calculate the sum of the first `k` elements and move on to the second combination, the calculation is mostly similar. The difference is that you are not adding the first element, but instead adding the next element to the combination. 

Therefore, we can construct the algorithm as follows:

1. calculate the sum of first `k` terms 
2. Iterate through the list, construct the current combination by subtracting the first element of the previous combination and adding the next element to the previous combination. 
3. for each iteration, compare and take the maximum value. 

At the end of the iteration, we will have found the maximum possible sum for a subarray of size k. We then divide this maximum sum by k to obtain the highest average.

## Codes 

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for j in range(1, len(nums)-k+1):
            current_sum = current_sum - nums[j-1] + nums[j+k-1]
            max_sum = max(max_sum, current_sum)
            
        
        return max_sum / k
```

## Complexity 

- the time complexity is `O(n)`, because we iterate though a list of length `n` at most once. 
- the space complexity is `O(1)`, beause we need to prepare two new variables to compare maximums. 