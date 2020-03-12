## 🧐 Problem
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.


### Example 1:
``` 
Input: s = "RLRRLLRLRL"
Output: 4
```

*Explanation*: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

### Example 2:
``` 
Input: s = "RLLLLRRRLR"
Output: 3
```

*Explanation*: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

### Example 3:
``` 
Input: s = "LLLLRRRR"
Output: 1
```
*Explanation*: s can be split into "LLLLRRRR".

### Example 4:
``` 
Input: s = "RLRRRLLRLL"
Output: 2
```

*Explanation*: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
 
## 💬 Approach
I was initially stuck on this problem for quite some time. I initially thought about what reasonable time complexities for my solution could be and work backwards, but I didn't understand the problem well-enough. 
After looking at a solution, I realized that since the entire string is already balanced, then if you extract a balanced substring from it you get another balanced substring regardless of size. Additionally, the string can only be broken up in-place, so you must work from end -> end.

## 🤓 Learnings 
In retrospect, it wouldn't be possible to have a faster solution than O(n) because we'd need to know the locations and contents of each char in the balanced string .
It would have also been helpful to start by listing everything that the problem definition tells me and everything I know about related problems/algorithms. This could be done (if completely stuck) by cycling through classical data structures and approaches and seeing whether or not they are applicable to the problem. Doing this both when stuck and when trying to optimize the solution would be ideal.