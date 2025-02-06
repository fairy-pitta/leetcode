# 0392 Is Subsequence 

## Problem URL 

https://leetcode.com/problems/is-subsequence/description/ 

## Problem Overview 

Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


### Example 1:
**Input:**  
`s = "abc"`, `t = "ahbgdc"`  
**Output:**  
`true`  

### Example 2:
**Input:**  
`s = "axc"`, `t = "ahbgdc"`  
**Output:**  
`false`  

### Constraints:
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.



## Solution 

For this problem, we want to be check two sequences concurrently. The main idea is that you want to match the character from each sequence one by one, and if it matches, move onto the next character. 

To do that, we will make use of the two pointers. 

- `s_cur` points to the current character in `s`
- `t_cur` points to the current character in `t`

The algorithm is as follows: 

1. If `s[s_cur]` matches `t[t_cur]`, move `s_cur` to the next character.
2. Always move `t_cur` to the next character, regardless of a match.
3. Continue this process until either:
   - `s_cur` reaches the end of `s`, meaning all characters of `s` are found in `t`, so return `True`.
   - `t_cur` reaches the end of `t` before `s` is fully matched, meaning `s` is **not** a subsequence, so return `False`.

### Corner Case

There are two possible corner cases. 
1. when `s` is an empty string. 
In this case, regardless of `t`, `s` is always a substring of `t`. So return True. 
2. when `t` is an empty string.
In this case, regardless of `s`, `s` is never a substring of `t`. So return False. 

it is important that we exclude the corner cases in this order, because in case where `s` and `t` are both empty, you want to return True. 

## Code 

```python 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_cur = 0
        t_cur = 0

        if len(s) == 0:
            return True 
        if len(t) == 0:
            return False

        while t_cur < len(t) and s_cur < len(s):
            if s[s_cur] == t[t_cur]:
                s_cur += 1 
            t_cur += 1 
        
        if s_cur == len(s):
            return True 
        return False
```

## Complexity 

the time complexity is O(m+n), because in the worst case, we iterate through `t` and `s` at most once. The maximum lengh of `s` is 100, so complexity for iterating through `s` is negligible, so it can be argued that that time complexity is O(m)
the space complexity is also O(1), because we just need two additional pointers. 

