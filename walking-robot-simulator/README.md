## 🧐 Problem

A robot on an infinite grid starts at point (0, 0) and faces north. The robot can receive one of three possible types of commands:

```
-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
```

Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays _on the previous grid square_ instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

### Example 1:

```
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
```

### Example 2:

```
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
```

_Note_:

```
0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
```

## 💬 Approach

The brain fog and fidgetiness was real with this one. I sat down and thought through my naive solution first, cycling through the commands and then if the command included movement, I cycled through all of the obstacles to check if the obstacle was in the direct line of movement between my starting and resulting positions. I checked this by holding either x or y constant depending on the direction of movement and checking if the remaining coordinate was bounded by pos and new_pos. Writing out my thoughts and drafting my initial solution took about 35 minutes. (😬) I found myself spending a lot of time brushing up on the correct syntax to execute the operations I was envisioning.

When met with a test case that included pages and pages of obstacles, I thought that it would greatly optimize my solution if I first cleaned the obstacles into two separate dictionaries: 1) a list of x-coordinates indexed by y-value, and 2) a list of y-coordinates indexed by x-value. In doing this, I was able to significantly restrict the set of obstacles to check that could have been obstructing my path. Rewriting my solution to leverage this data took me to about 1 hour and 20 mins, including a few short breaks. My code still has lots of room for consolidation and optimization, but I'm happy with this as a first problem back given it's 35% acceptance rate.

## 🤓 Learnings

This problem was a lot of review and getting back into the interviewing mindset after a long hiatus. I did not vocalize my process as much as I should have, nor did I assess my alternatives by time complexity and brainstorm potentially useful data structures. I've got quite a ways to go, but some progress is better than no progress. ✌️
