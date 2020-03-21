class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """ Patterns:
           - All single-digit primes are self-dividing
           - All numbers that are just the same digit repeated, are self-dividing
           - All numbers
           - All multi-digit primes are not self-dividing
           - All numbers divisible by 10 are not self-dividing
           Test cases:
           left = 20, right = 40:
           => 22, 24, 33, 36
           Hypothesis: all digits must be multiples that are <= the last digit
           False: 428 and 39 both break this

           left = 40, right = 60:
           => 44, 48, 55
           Patterns: If a number contains both 5 and 2, then it can't be self-dividing (divisibility by 5 and 2 implies divisibility by 10, which is not allowed)

           left = 60, right = 80:
           => 66
           Patterns: The first number that is self-dividing when increasing throughout a range is the number where the digit next to the first that is equal to the first (i.e. [60-65] can't be self-dividing since [0-5] < 6 and we need the number to be divisible by 6 )
           - Numbers containing 5,6,7,8, or 9 can only be self-dividing if these numbers show up (at least) in the last digit

           left = 100, right = 150:
           => 111, 112, 115, 122

           [ Out of time ]
       """

    """ Optimized solution 1:
        -
    """

    """ Naive solution:
        - For each number from left -> right, manually check if it is self-dividing
    """

    def self_dividing(n):
        for d in str(n):
            if int(d) == 0: return False
            if n % int(d) != 0: return False
        return True

    return [n for n in range(left, right + 1) if self_dividing(n)]

