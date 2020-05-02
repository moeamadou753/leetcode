## 🧐 Problem
In a 2 dimensional array grid, each value `grid[i][j]` represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

### Example:
```
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
```
### Explanation: 
The grid is:
``` 
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
```
The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

*Notes*:
``` 
1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
```

## 💬 Approach
This was my first problem-solving exercise in roughly 2 weeks (outside of work). I was a little bit rusty with Python syntax, but I think I did pretty well, given that I completed the medium problem in 20 minutes, clearly vocalizing my thought-process along the way and not getting stumped.
I first had to understand what the problem meant by viewing from top/bottom or left/right, I didn't initially know whether that meant from inside or outside the grid, but after giving it some thought I realized inside the grid wouldn't make sense since you aren't guaranteed that a taller building isn't behind you! It was then clear that you would have to keep track of the tallest building for both the current column and row. I did this by creating a dictionary of column indices to max building heights and populated it when moving through the first row (I would simply iterate through all of the rows and add `row[index]` to the a temp list, then sort that list and return the highest element). Then, when evaluating each row, I would first create a copy of the row, sort it and take the max element, then for each element in the row I would add `min(max_lr, max_tb) - item` to an accumulator variable. I did this until we had visited all elements of the list of lists.

## 🤓 Learnings 
I actually learned quite a bit from reflecting on my own and other solutions to this one. I learned about:
- The equivalent of the javascript spread operator (`iterable...`), which is (`*iterable`). It simply destructures the iterable for use as parameters in a function, among othere things 
- A neat way to transpose lists of lists (using `zip(*lol))`)
- You can call `min()` or `max()` on an iterable in python. This is a much more idiomatic approach then sorting a list and accessing the first/last element
- This definitely wasn't as painful as I thought it'd be after a sizeable break. Excited to keep getting better! ✨🎉
