class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """ Given from problem:
            - Have to visit points in array order => greedy algorithm or memoization
            - Diagonal movement and single-axis movement equally costly => simple euclidean distance problem

            Proposed solution:
            - Cycle through list of points and calculate euclidean distance between curr and next
            - Add time to visit next from curr to solution accumulator
            - Repeat until end of list is reached
            Time complexity: O(n)
            Space complexity: ~ O(1)

            Encountered issue: Euclidean distance won't always be a perfect integer
            Proposed workaround: Create primitive euclidean distance algorithm that uses 'legal' moves
            Runtime: 64ms (25th percentile)
        """
        # solSoFar=0
        # for i, coord in list(enumerate(points))[:len(points) - 1]:
        #     if points[i+1] is not None:
        #         diagonal = (min(abs(points[i+1][0] - points[i][0]),
        #                         abs(points[i+1][1] - points[i][1])))
        #         diagonal = [diagonal if points[i+1][0] > points[i][0] else -diagonal,
        #                     diagonal if points[i+1][1] > points[i][1] else -diagonal]
        #         solSoFar += abs(diagonal[0]) + abs(((points[i+1][0] - points[i][0]) - diagonal[0]) +   ((points[i+1][1] - points[i][1]) - diagonal[1]))
        # return solSoFar
        """ Optimized Solution 1:
            - Reduce number of operations, make less convoluted, use more meaningful var names
            Runtime: 56ms (83rd percentile)
        """
        time = 0
        for i in range(len(points) - 1):
            start = points[i]
            end = points[i + 1]
            diagonal = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
            time += diagonal
            time += abs(end[0] - start[0]) - diagonal + abs(end[1] - start[1]) - diagonal

        return time