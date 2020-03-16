class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        """ Optimized solution 2:
            - Evaluate row and coloperations individually
            - Take the sum of odds from columnal and row-wise operations
            - Subtract negated counts (wherever an odd row-wise op and odd column-wise op has been found, remove both from our count)
        """
        rowop, colop = [i[0] for i in indices], [i[1] for i in indices]
        set_row, set_col = set(rowop), set(colop)
        a, b = sum(rowop.count(i) % 2 for i in set_row), sum(colop.count(i) % 2 for i in set_col)
        return m * a + n * b - 2 * a * b

        """ Optimized solution 1:
            - Create a dictionary for row increments and column increments
            - Iterate through those two dictionaries the same you would a matrix
            - Compare sums at each point and increment counter
            Time complexity: O(n*m + k) where k is the number of indices
        """
        #         row_inc = {i:0 for i in range(n)}
        #         col_inc = {j:0 for j in range(m)}

        #         for index in indices:
        #             if index[0] in row_inc: row_inc[index[0]] += 1
        #             if index[1] in col_inc: col_inc[index[1]] += 1

        #         num_odd = 0
        #         for row in row_inc.values():
        #             for col in col_inc.values():
        #                 if (row + col) % 2 != 0: num_odd += 1

        #         return num_odd

        """ Naive solution:
            - Store indices in a dictionary with a pair key representing the x and y coord of the element in question
            - Iterate through the dictionary of indices applying the k operations
            Time complexity: O(n*m*k), where k is the number of indices
        """
#         cells = {}
#         for index in indices:
#             for i in range(m):
#                 if (index[0], i) in cells: cells[(index[0], i)] += 1
#                 else: cells[(index[0], i)] = 1
#             for j in range (n):
#                 if (j, index[1]) in cells: cells[(j, index[1])] += 1
#                 else: cells[(j, index[1])] = 1

#         odd_cells = 0
#         for cell in cells.values():
#             if cell % 2 != 0: odd_cells += 1

#         return odd_cells