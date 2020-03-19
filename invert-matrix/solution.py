class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """ Alternate solution:
            - Invert the array and then use array slicing to reverse
        """
        res = []
        for row in A:
            inv = [1 if i == 0 else 0 for i in row]
            inv = inv[::-1]
            res.append(inv)

        return res
        """ Optimized solution 1:
            - Leverage list comprehension for one-liner
            Rationale:
            - It isn't possible to have a solution faster than O(n*m) since in order to reverse and toggle each element, we must view all n*m elements at least once 
        """
        # result = [[1 if A[x][y] == 0 else 0 for y in range(len(A[0]) -1, -1, -1)] for x in range(len(A))]
        # return result
        """ Naive solution:
            - Reverse each of the row columns while inverting them in place
        """
        # result = []
        # for x in range(len(A)):
        #     nextRow = []
        #     for y in range(len(A[0]) - 1, -1, -1):
        #         nextRow.append(1 if A[x][y] == 0 else 0)
        #     result.append(nextRow)
        # return result