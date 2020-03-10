from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """ Dumb solution:
            - Convert integer into list of digits by dividing by 10 in for loops
            - Sum and multiply list using list comprehension
        """

        """ Naive solution:
            - Convert integer into string
            - Sum and multiply list of digits using list comprehension
        """
        digifiedList = [int(x) for x in str(n)]
        product = reduce((lambda curr, rest: curr * rest), digifiedList)
        addition = sum(digifiedList)

        return product - addition