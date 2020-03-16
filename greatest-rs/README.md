## 🧐 Problem
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

### Example 1:
``` 
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
```

*Constraints*:
``` 
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
```

## 💬 Approach
My solution accomplished the task in the minimal time of O(n) (you must visit each element of the array at least once). I simply started from the right-side and made my way to the left-side, keeping track of the greatest element to the right so far.
