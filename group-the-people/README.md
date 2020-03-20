## 🧐 Problem
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

### Example 1:
``` 
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
```

### Example 2:
``` 
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```
 

**Constraints**:
``` 
groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n`
```

## 💬 Approach
My initial approach was very basic. I first cleaned the array into a dictionary where the keys were group sizes and the values were a list of IDs with that group size. I then iterated through those lists to create my groups and appended to the final solution after each grouping.

## 🤓 Learnings 
I came across another approach that turned my ~20 line code to 3 lines using `collections.defaultdict(type)` -- a python data structure that essentially gets rid of key errors. Whenever accessing the element k in the dictionary, it assumes that the value is of type `type` and generates the empty state of this key and value.

I will remember to try and implement array slicing wherever it makes sense, as it can lead to the simplification of a lot of code. 

