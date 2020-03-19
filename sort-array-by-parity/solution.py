class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """ Alternate solution:
            - Same idea but use two pointers to halve work in best case
        """
        left, right = 0, len(A) - 1
        while left < right:
            if A[right] % 2 == 0:
                if A[left] % 2 == 0:
                    left += 1
                else:
                    A[left], A[right] = A[right], A[left]
            else:
                right -= 1
        return A

        """ Naive Solution:
            - Use a pointer to keep track of last even number
            - Swap elements throughout the array to the index past the last even number
            Time Complexity: O(n)
        """
#         even_ptr = 0

#         for i in range(len(A)):
#             if not A[i]&1:
#                 temp = A[even_ptr]
#                 A[even_ptr] = A[i]
#                 A[i] = temp
#                 even_ptr += 1

#         return A