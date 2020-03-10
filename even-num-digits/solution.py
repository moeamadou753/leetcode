class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """ Immediate solution:
            - Turn numbers into strings and check length of strings divisible by 2
            - Use list comprehension to create an array of 1's representing even strings
            - Sum the list of 1's
            Time Complexity: O(n)
        """
        return sum([1 for num in nums if len(str(num)) % 2 == 0])
