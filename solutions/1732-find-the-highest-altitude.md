# 1732. Find the Highest Altitude

## Problem URL

[https://leetcode.com/problems/find-the-highest-altitude/](https://leetcode.com/problems/find-the-highest-altitude/)

## Problem Overview

A biker is going on a road trip that consists of `n + 1` points at different altitudes. The biker starts his trip at point `0` with an initial altitude of `0`.

You are given an integer array `gain` of length `n`, where `gain[i]` represents the net gain in altitude between points `i` and `i + 1`. Your task is to return the **highest altitude** reached during the trip.

### Example 1:
**Input:**  
`gain = [-5,1,5,0,-7]`  
**Output:**  
`1`  
**Explanation:**  
The altitudes are `[0, -5, -4, 1, 1, -6]`. The highest altitude reached is `1`.

### Example 2:
**Input:**  
`gain = [-4,-3,-2,-1,4,3,2]`  
**Output:**  
`0`  
**Explanation:**  
The altitudes are `[0, -4, -7, -9, -10, -6, -3, -1]`. The highest altitude reached is `0`.

## Constraints:
- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`


## Solution 

	1.	Start at altitude 0.
	2.	Iterate through gain, adding each value to the previous altitude, hence obtaining the current altitude. 
	3.	Keep track of the maximum altitude reached.
	4.	Return the highest altitude at the end.

## Code 

```python 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        for i in range(len(gain)):
            if i != 0:
                gain[i] = gain[i] + gain[i-1]
            max_altitude = max(max_altitude, gain[i])
        
        return max_altitude
```


## Complexity 

Time complexity is `O(n)` because we iterate though the list of length `n` at most once 
Space complexity is `O(1)` because we prepare an extra variable. 