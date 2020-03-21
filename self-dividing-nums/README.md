## 🧐 Problem
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

### Example 1:
``` 
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
```

**Note**:
``` 
The boundaries of each input argument are 1 <= left <= right <= 10000.
```

## 💬 Approach
Brute force

## 🤓 Learnings 
It is always in your best interest to get working code down first before you try and optimize. This shows that in a professional setting, that you'll be able to get an MVP working without letting perfectionism get in the way. While I was able to come up with a variety of rules that could tell that a number was or was not self-dividing, I wasn't able to come to a 'theory of everything' per se, that tied them all together. The only provided solution was also brute force.

I'm glad that I went with the approach of getting down my naive solution first and then thinking through optimization afterwards.  