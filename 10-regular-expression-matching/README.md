# 10. Regular Expression Matching

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:
- `'.'` Matches any single character.​​​​
- `'*'` Matches zero or more of the preceding element.

The matching should cover the __entire__ input string (not partial).

 
### __Example 1:__
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### __Example 2:__
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

### __Example 3:__
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```
 

### __Constraints:__
- `1 <= s.length <= 20`
- `1 <= p.length <= 30`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'.'`, and `'*'`.
- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.


## __Results:__

Runtime: _2403 ms_, faster than _5.00%_ of Python3 online submissions for Regular Expression Matching.
Memory Usage: _14.2 MB_, less than _23.72%_ of Python3 online submissions for Regular Expression Matching.
|Status|Runtime|Memory|
|---|---|---|
|Accepted|2403 ms|14.2 MB|

