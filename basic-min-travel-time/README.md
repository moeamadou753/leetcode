## 🧐 Problem
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
 

### Example 1:
```
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```
### Example 2:
```
Input: points = [[3,2],[-2,2]]
Output: 5
```

*Constraints*:
```
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
```

## 💬 Approach
This was mostly a math problem. I initially ran into difficulty under the assumption that diagonal moves could only be made if delta y and delta x were of the same sign. This wasn't the case, but rather a diagonal move can be made whenever delta y and delta x isn't 0, so if you just take the min of the magnitudes of delta y and delta x, then you always get your maximum diagonal travelled.

## 🤓 Learnings 
I was definitely starting to feel some fatigue when coming into this problem. I had been up late at night to get my problem of the day in and I could tell that I was sharp and not clearly-thinking during this one.

I think what I need to keep in mind especially as co-op ends and the demands of school, extracurriculars, and the job hunt approach is to always be objective when evaluating my progress towards my goals for the term. It is very easy to beat up on yourself because you're not seeing sufficient progress every day, but zooming out, planning ahead, and making sure you're still on schedule can allow you the space to not have to be 100% every single day and be okay with that, knowing that the overall pattern is much more important than any one anomaly.