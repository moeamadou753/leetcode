class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """ Know we'll probably be using list comprehension
                - How to filter strings with sequential digits
                    - Bit shifting (is there a pattern with bin ints of sequential digits?)
                        - 123 = 1111011
                        - 12 = 1100
                        - 23 = 10111
                        - Not really
                    - Modulus in a while loop (would be O(n*k)) where k is the length of each string of ints
                    - Since sequence can be broken at any point within the number, we must check that each digit is in place
                    - ** We could take the length of each string and then extrapolate the number it must be equal to in order for it to be sequential; we do this by generating a range and then casting that to an integer? **
                - How to filter strings outside a given range
                    - Sort and then remove all outside of bounds (O(nlogn + n))
                    - Sort and then binary search for the closest items to bounds and remove everything past those indices(O(nlogn))
                    - Can do it in O(n) without sorting by just going through each element and checking whether or not it is inside the bound
                    - Can we do it in O(logn)? No we have to check every individual element (check assumption afterwards)
                    - Since it needs to be sorted we will take the Onlogn solution

        """
        # Solution: Merge sort while checking that each element we are placing is in the range and is a sequence of digits (16m)
        # for i in range(len())
        # I just realized that I completely misinterpereted the question.

        """ - Need to know when we have gone too far in terms of building out sequentiaal integers
                - If low and high are the same length, then we must stop at the integer whose digits are all <= the corresponding digit of high
                - If low and high are not of the same length, then we must stop at the (21m - Hint #1)
                - Can do it in O(n) by generating all integers that are roughly within the range and then checking the range for the ones that are the same length as low and high
        """
        res = []
        # Assuming that the ranges are inclusive both ways; guess not
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(1, 9 - i + 2):  # Needed to be updated
                # Freezing because I don't understand how to efficiently convert a range into a numbers' digits in python. Reviewing list comprehension => will need to use reduce (python equivalent of foldl)
                # Best way to find place value? Will take index of the array to increment places or find how many times 10 goes into the accumulator by turning it into a string and finding its length
                # Top-down approach is better. (Feel dumb rn) multiple acc by 10 and add x
                n = reduce(lambda acc, x: acc*10 + x, range(j, j + i))
                if i == len(str(low)) or i == len(str(high)):
                    # if low > n:
                    #     continue
                    # if n > high:
                    #     break
                    # else:
                    if low <= n <= high:
                        res.append(n)
                else:
                    res.append(n)
        # Checking code 35m 50s; Done checking first pass 39m: 14s; Made corrections (off by 1 errors) 47m 30s
        return res

        """ Faster solution: 
            - Generates all sequential digits smaller than the upper bound and only adds the ones greater than the lower bound
            - Uses a higher order function to sort afterwards
            
            # class Solution:
            #     def sequentialDigits(self, low: int, high: int) -> List[int]:
            #         ans = []
            #         for i in range(1, 9):
            #             while i < high and (rem := i%10):
            #                 if i >= low:
            #                     ans.append(i)
            #                 i = (i*10) + rem + 1
            #         return sorted(ans)
        """
