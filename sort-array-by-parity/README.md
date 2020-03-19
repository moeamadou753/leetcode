## 🧐 Problem
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

### Example 1:
``` 
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```
 

**Note**:
``` 
1 <= A.length <= 5000
0 <= A[i] <= 5000
```

## 🤓 Learnings 
Two-pointer approaches to problems have always seemed so intimidating. I learned how two-pointer solutions require more operations per iteration, but lead to half the iterations. Using a two-pointer approach can seem like over-engineering but it pays off as n grows very large.