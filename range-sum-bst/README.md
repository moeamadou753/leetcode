## 🧐 Problem
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


### Example 1:
```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:
```
``` 
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

*Note*:
``` 
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
```

## 💬 Approach
This is a problem that I've seen many times before, but I found myself struggling to remember how to implement various tree traversal and searching algorithms. (depth-first search, breadth-first search, pre-order, in-order, post-order) My first naive solution was a simple in-order traversal with no range checking. I optimized that further by not going lower than L or higher than R. 

## 🤓 Learnings 
For some reason, there were huge performance disparities when recursing on a helper function vs. recursing on the main solution function. Still not sure why because the algorithm is the exact same, but I'm guessing that it has something to do with how python3 handles stack frames.