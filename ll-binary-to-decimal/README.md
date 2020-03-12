## 🧐 Problem
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

### Example 1:
```
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```

### Example 2:
```
Input: head = [0]
Output: 0
```

### Example 3:
```
Input: head = [1]
Output: 1
```

### Example 4:
```
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
```

### Example 5:
``` 
Input: head = [0,0]
Output: 0
```
 
### Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

## 💬 Approach
1. Turning the binary number into a dictionary, using the indices as keys and the binary digit as values then iterating through the dictionary.
2. Use bitwise operators (shift, or) and iterate through the linked list only once.

## 🤓 Learnings 
Bitwise operators can be really useful whenever we are dealing with binary structures. Here is a table of bitwise commands for reference:

| Operator | Description | Example|
|:---------|:-----------:|:------:|
| & (Binary AND) | Operator copies a bit to the result if it exists in both operands | (0011 1100 & 0000 1101) =  1100 |
| \| (Binary OR) | Operatior copies a bit if exists in either operand | (0011 1100 \| 0000 1101) = 0011 1101 |
**Incomplete, referencing: https://www.tutorialspoint.com/python/bitwise_operators_example.htm**