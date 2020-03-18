## 🧐 Problem
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
```
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
```
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

### Example 1:
```
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
```

### Example 2:
```
Input: s = "1326#"
Output: "acz"
```

### Example 3:
```
Input: s = "25#"
Output: "y"
```

### Example 4:
```
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
```

*Constraints*:
```
1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
```

## 💬 Approach
This is a problem that seems very simple at first glance. I simply decoded the string as one would semantically -- leading to an egregious solution. 

## 🤓 Learnings 
Though this should have been a rather easy problem to solve, I struggled quite a bit with the array slice syntax and behaviour. I learned that:
- `a[-x:]` returns a slice of the last x items in a. 
- `a[:x]` returns a slice of the first x items in a.
- `a[x:]` returns a slice of a from position x (inclusive) to the end.
- `a[:-x]` returns a slice of a with the last x items removed.
When wanting to remove the last element from an array, `a[second_last + 1:]` will cause an index out of bounds error while `a[:-1]` will not. 