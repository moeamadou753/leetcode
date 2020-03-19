class Solution:
    def sumZero(self, n: int) -> List[int]:
        """ Optimized Solution 1:
            - Cast a the range of [-n/2, n/2] to a list
            - Pop zero from that list if n % 2 == 0
            24ms (96.7 percentile)
        """
        result = list(range(-int(n / 2), int(n / 2 + 1)))
        if n % 2 == 0:
            result.remove(0)
        return result

#         """ Naive Solution:
#             - Check if n is even or odd and then
#             - If odd, the array will contain 0 and (n-1)/2 positive-negative pairs
#             - If even, the array will contain n/2 positve negative pairs
#             Time: 32ms
#         """
#         vectors = [-1,1]
#         result = [] if n % 2 == 0 else [0]

#         result.extend([ n*v for n in range(1,n,2) for v in vectors])

#         return result
