## 🧐 Problem
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


### Example 1:
``` 
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
```

### Example 2:
``` 
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
```

### Example 3:
``` 
Input: matrix = [[7,8],[1,2]]
Output: [7]
```
 
**Constraints**:
``` 
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
```

## 💬 Approach
Create a list of row mins and col maxs using list comprehension and then convert those lists to sets using set(). Finally, return the intersection of the set.

## 🤓 Learnings 
List comprehension can allow you to pass elements if a condition isn't met when you structure your list comprehension as `[x for x in list if cond]`  INSTEAD OF `[x if cond else None for x in list]`. 
I learned about the term [duck-typing](https://en.wikipedia.org/wiki/Duck_typing) , which is simply how functions evaluate whether or not their parameters are of valid types in dynamically-typed language. The premise is that if the data is structured in a way where the function call makes sense, then it'll work.