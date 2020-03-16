## 🧐 Problem
Given a string s. You should re-order the string using the following algorithm:

1. Pick the smallest character from s and append it to the result.
2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the largest character from s and append it to the result.
5.  Pick the largest character from s which is smaller than the last appended character to the result and append it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from s.
8. In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

### Example 1:
``` 
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
```

### Example 2:
``` 
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
```

### Example 3:
``` 
Input: s = "leetcode"
Output: "cdelotee"
```

### Example 4:
``` 
Input: s = "ggggggg"
Output: "ggggggg"
```

### Example 5:
``` 
Input: s = "spo"
Output: "ops"
```
 
*Constraints*:
``` 
1 <= s.length <= 500
s contains only lower-case English letters.
```

## 💬 Approach
I started with the naive approach of first sorting the string into a char array and iterating through the remainder of the array each time to find either the next biggest char or smallest depending on the step of the process. This quickly became quite verbose and I switched to a more elegant solution where I only had to iterate through the array once and keep track of all of the letters in a dictionary-style list of chars where the keys represented the letter as an index of the  alphabet and the values represented the number of occurrences of that letter in the remainder of the string. We then iterate through this alphabetical array with a flag to let us know whether or not we are appending in increasing or decreasing order until the remainder of the array is empty.

## 🤓 Learnings 
I learned about some python functions for unicode functionalities: namely, ord and chr. I also learned that once again, defaulting to an approach leveraging dictionaries for constant time access to elements of interest can almost always lead to optimization in a problem with a solution >= O(n) time complexity.