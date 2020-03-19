## 🧐 Problem
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.


Example 1:
``` 
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
```
 

**Constraints**:
``` 
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
```

## 🤓 Learnings 
You can quickly check for divisibility by 2 by using the bitwise AND operator! The expression `(num & 1)` returns the intersection of bits between the binaries of the number and 1 (i.e. 10010 representing 10, & 1 returns 0 since 10 does not have a 1 in its first-place. Similarly, 101 & 1 returns 1) I learned about [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) implementations in python using arrays.

Learn more about other data structures used for stack implementations in python:
- [Collections](https://docs.python.org/2/library/collections.html)
- [Queues](https://docs.python.org/2/library/queue.html)