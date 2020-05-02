"""
    Attempt 1: Faster than 15% of solutions, uses less memory than 5%
    Time taken: 20 mins.
"""
#
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#         """ Initial thinking:
#             - keep track of LR skyline and TB skyline
#             - Max target height is min(LR, TB)
#             - Store indices in map as (i, j): val
#             - Go along row, finding columnal max at each step (O(i x j) for finding both LR and TB concurrently)
#             - Iterate through each row item, increasing to min(LR, TB)
#             OR
#             - For each row, quicksort a copy of it and take the max to find LR (O nlogn)
#             - Create a copy of the column and quicksort / take max of it to find TB (On + Onlogn => Onlogn)
#                 - Store column values in dictionary to optimize for rest of solution
#             - For each element in the row, set to min TB(c) and LR(r)
#
#         """
#         tb_col = {}
#         addedheightsofar = 0
#         for row_num, row in enumerate(grid):
#             rowcp = row.copy()
#             rowcp.sort()
#             lr_row = rowcp[-1]  # Gets last element of list
#
#             for index, item in enumerate(row):
#                 if row_num == 0:
#                     listcp = []
#                     for row_lr in grid:
#                         listcp.append(row_lr[index])
#                     listcp.sort()
#                     tb_col[index] = listcp[-1]
#                 target = min(tb_col[index], lr_row)
#                 addedheightsofar += max(item, target) - item
#                 item = max(item, target)
#                 row[index] = item
#         return addedheightsofar

"""
    Better solution #1 by @junaidmansuri : 
    https://leetcode.com/problems/max-increase-to-keep-city-skyline/discuss/445773/Python-3-(two-lines)-(beats-~100)
    
    Missing knowledge:
    - Tuple destructuring in python3 (super cool!)
    - Unpacking argument lists (like spread operators in javascript :zoom-eyes:)
    - The zip function (essentially transposes a list of lists 😍)
    - Cartesian products via Python itertools library (honestly a lil confusing: https://docs.python.org/3/library/itertools.html)
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, G: List[List[int]]) -> int:
        M, N, R, C = len(G), len(G[0]), [max(r) for r in G], [max(c) for c in zip(*G)]
        return sum(min(R[i], C[j]) - G[i][j] for i, j in itertools.product(range(M), range(N)))

"""
    Better solution #2 by @noobie12:
    https://leetcode.com/problems/max-increase-to-keep-city-skyline/discuss/591404/Python-Basic-Solution-Faster-than-92
    
    Missing knowledge:
    - Unpacking argument lists (like spread operators in javascript :zoom-eyes:)
    - The zip function (essentially transposes a list of lists 😍)
    - You can call min or max on a list! Don't have to sort it first and then get the first/last item
    
"""
# class Solution:
#     def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
#
#         matrix_row, matrix_col, final_result = [], [], []
#         for row in grid:
#             # matrix_row -> list containing the maximum element for each row in the grid
#             matrix_row.append(max(row))
#         for col in zip(*grid):
#             # matrix_col -> list containing the maximum element for each column in the grid
#             matrix_col.append(max(col))
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 val = min(matrix_row[i], matrix_col[j])
#
#                 if val != grid[i][j]:
#                     # Only the value of increase has to be considered towards the final sum
#                     final_result.append(val - grid[i][j])
#
#         return sum(final_result)