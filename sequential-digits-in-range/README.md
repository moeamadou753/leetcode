## 🧐 Problem

An integer has _sequential digits_ if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range `[low, high]` inclusive that have sequentiaal digits.

**Example 1:**

```
**Input:** low = 100, high = 300
**Output:** [123,234]
```

**Example 2:**

```
**Input:** low = 1000, high = 13000
**Output:** [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints:**
`10 <= low <= high <= 10^9`

## 💬 Approach

I initially misinterpereted the problem as being given an array of strings and needing to filter out those that don't have sequential digits and aren't within a given range. After writing the pseudocode for this solution (20m mark), I realized that I had misinterpreted the question and tried to pivot towards solving the actual problem with the approach I had written down.

The idea was that I can do this in O(n) time by iterating between the lengths of digits of the lower and upper bounds and only checking whether or not the produced integer was in the range if it matched the length of one of the bounds. I used the higher order function reduce, which is essentially the python3 equivalent of foldl. I had written my solution after 15m 50s and dealt with off-by-1 and runtime errors by the 27m 30s mark.

## 🤓 Learnings

This was my first problem in a while, and man do I feel rusty. I am liking the approach of writing down questions as I code to help me vocalize my thought process, but also for the purpose of research after completing the problem so that I can build new knowledge that will allow me to more elegantly solve future problems. This was mainly review for me in terms of python syntax and converting a list of digits into an integer using foldl. I definitely have a huge amount of studying to do before I am back at the foundational knowledge levels to glide through medium's and make honest cracks at hard's.
