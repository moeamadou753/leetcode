## 🧐 Problem
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

## 💬 Approach
I started by stepping through various input values. Thinking that the solution of arrived at by following the problem definition 1:1, was too on-the-nose, I tried to remove the highest divisible power of two at each step. 

This involved finding the nearest power, y, of two <= x by taking floor(log2(x)) and then finding the gcd of x and y. 

## 🤓 Learnings 
My use of the gcd function—which has a runtime of O(log(n)) —significantly slowed down the performance of my solution. The brute-force solution had a runtime of O(n) whereas my more convoluted solution sat at O(n log(n)). 

I think that my main takeaway moving forward is that it'll save me a lot of frustration to first jot down the time and space complexities of potential optimizations to a problem before actually coding them. Moreover, it's important to make sure that you're always moving towards better understanding the problem. It can be palpably paralyzing to be stuck—silently standing at a whiteboard with an urgent yet defeated demeanor. At the same time, it can be just as demoralizing asking for too many hints as you work through a problem; so, the better approach may be to start with idiomatic pseudocode and annotate your significant computations with time and space complexities as you go. Once you've written a solution that you know you can code, either refine it further by checking that your time and space complexities are reasonably optimal, or get to coding! 

To me, this is more productive than desperately grasping for random pieces of knowledge and realizing, after 30 minutes to be sure, that you've come up with absolutely nothing. A systematic approach will prompt mental associations to data structures and classical algorithms that you've seen way back when.
