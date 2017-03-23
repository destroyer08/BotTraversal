Solution Approach:

I am using dynamic programming approach, where I have to pre process the given matrix in another matrix called trace matrix.
In trace matrix element at location i,j represents the minimum distance from 0,0 to i,j. To fill trace matrix I converted given 
hex number into integer for simple calculation.
Another way to solve is greedy approach where we could lead to wrong path and no gurantee for right answer or we could use
bruteforce where we can traverse all possible paths and then select shortest path but with cost of higher time complexity. So 
I chose DP approach.
Complexity Analysis: 
Let say n is number of rows and m is number of columns in give grid.

Trace Matrix
Time complexity O(n*m) and Space complexity O(n*m). Solution prints the path direction for bot at each step.

Traverse Bot
Time Complexity O(n+m) and space complexity O(1)

Overall
Time Complexity O(n*m) and Space complexity O(n*m)
