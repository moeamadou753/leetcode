class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """ Initial naive solution:
            - Use pointer for both x and y axes, stop when next number >= 0
        """

        num_negatives = 0

        for y in range(len(grid) - 1, -1, -1):
            for x in range(len(grid[y]) - 1, -1, -1):
                if grid[y][x] >= 0: continue
                num_negatives += 1
            if grid[y][x] >= 0: continue
        return num_negatives

        """ Optimized solution 1:
            - Use binary search to find the largest element less than 0
            - Extrapolate the number of negative numbers by taking the number of 
              remaining elements in the 2D array
        """
