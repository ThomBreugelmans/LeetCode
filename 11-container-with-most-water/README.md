# 11. Container With Most Water

You are given an integer array `height` of length `n`. There are n vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store._


__Notice__ that you may not slant the container.
 

### __Example 1:__
![example](example_1.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### __Example 2:__
```
Input: height = [1,1]
Output: 1
```
 

### __Constraints:__

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 10^4`



## __Results:__

Runtime: _845_ ms_, faster than _69.90%_ of Python3 online submissions for Regular Expression Matching.
Memory Usage: _27.6 MB_, less than _22.34%_ of Python3 online submissions for Regular Expression Matching.
|Status|Runtime|Memory|
|---|---|---|
|Accepted|845 ms|27.6 MB|