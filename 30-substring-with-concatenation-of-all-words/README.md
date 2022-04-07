# 30 Substring with Concatenation of All Words

You are given a string `s` and an array of strings `words` of __the same length__. Return all starting indices of substring(s) in `s` that is a concatenation of each word in `words` __exactly once__, in any order, and __without any intervening characters__.

You can return the answer in __any order__.

### __Example 1:__
```
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

### __Example 2:__
```
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
```

### __Example 3:__
```
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
```

### __Constraints:__

- `1 <= s.length <= 10^4`
- `s` consists of lower-case English letters. 
- `1 <= words.length <= 5000` 
- `1 <= words[i].length <= 30` 
- `words[i]` consists of lower-case English letters.


## __Results:__

Runtime: _845 ms_, faster than _69.90%_ of Python3 online submissions for Regular Expression Matching.
Memory Usage: _27.6 MB_, less than _22.34%_ of Python3 online submissions for Regular Expression Matching.
|Status|Runtime|Memory|
|---|---|---|
|Accepted|845 ms|27.6 MB|
