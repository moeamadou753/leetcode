class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """ Naive solution, find the largest element by stepping through the rest of the array
            O(x * sum(len (n - x))
        """
        """ Optimized solution 1:
            - Start from the right and keep track of the largest element so far
            Time complexity: O(n)
        """
        biggestSoFar = -1
        for i in range(len(arr) -1,-1,-1):
            temp = arr[i]
            arr[i] = biggestSoFar
            if temp > biggestSoFar : biggestSoFar = temp
        return arr