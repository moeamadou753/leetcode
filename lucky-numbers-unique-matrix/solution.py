class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """ Optimized solution 1:
            - Turn row_mins and col_maxs into sets for O(1) element access since items are unique
            - Return the intersection of the two sets
            Runtime: 132ms
        """
        row_mins = set([ min(row) for row in matrix ])
        col_maxs = set([ max([matrix[row][col] for row in range(len(matrix))]) for col in range(len(matrix[0]))])
        return row_mins.intersection(col_maxs)
        """ Naive Solution: 
            - Create a list of row minimums and a list of column maxes
            - Remove all the elements in the first list if not in the second list
            Time complexity: O(m*n +  m + n) ~= O(m*n)
            Runtime: 140ms
        """
        # row_mins = [ min(row) for row in matrix ]
        # col_maxs = [ max([matrix[row][col] for row in range(len(matrix))]) for col in range(len(matrix[0]))]
        # # Could also transpose matrix and use the same list comprehension with max
        # return [ e for e in row_mins if e in col_maxs]