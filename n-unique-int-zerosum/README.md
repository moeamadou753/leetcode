## 🧐 Problem
Given an integer n, return any array containing n unique integers such that they add up to 0.

 
### Example 1:
``` 
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
```

### Example 2:
```
Input: n = 3
Output: [-1,0,1]
```

### Example 3:
``` 
Input: n = 1
Output: [0]
```

 

**Constraints**:
``` 
1 <= n <= 1000
```

## 🤓 Learnings 
The range function returns an iterable, not a list! You'll need to cast it before you can return it as a valid solution. The top boundary of the range function is also exclusive, so it's important to watch out for potential off-by-1 errors. **list.pop** removes an element at a specific index while **list.remove** removes the first occurrence of the specified element. Similarly, list.push doesn't exist but **list.insert** and **list.append** mirror the additive inverse of the aforementioned behaviour.