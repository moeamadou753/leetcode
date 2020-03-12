# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """ Initial thought: Problem will involve some sort of recursion because of ListNode structure
            After some thinking: We get an O(n) solution by flattening decimal value into a dictionary and then iterating from the end of that dictionary to the beginning. I'd call this the naive solution
        """
        #         flattenedBinary = {}
        #         ptr = 0
        #         while head is not None:
        #             flattenedBinary[ptr] = head.val
        #             head = head.next
        #             ptr += 1

        #         solutionSoFar = 0
        #         for i in range(ptr - 1, -1, -1):
        #             solutionSoFar += flattenedBinary[i] * 2 ** (ptr - 1 - i)

        #         return solutionSoFar

        """Optimization 1: Use bit-shifting! Still O(n), but half the operations (at least over the hood) and a LOT cleaner"""
        sol = 0
        ptr = head

        while ptr:
            # << is the left bitwise 'shift' operator : it returns left*2^right
            # | is the bitwise 'or' operator : it compares the two numbers in binary and creates a new binary with 1's in all of the places that appear in the union of the two binaries (i.e. 1010 | 101 = 1111)
            sol = (sol << 1) | ptr.val
            ptr = ptr.next
        return sol


