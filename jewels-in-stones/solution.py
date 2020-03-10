class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """ Naive Solution:
            - Step through the string S and check if each char is in J, keeping a tally as you go
            Time complexity: O(n*k)
        """
        #         n = 0
        #         for s in S:
        #             if s in J:
        #                 n+=1
        #         return n

        """ Optimized solution 1 (Requires knowledge of sum function): 
            - Use list comprehension
        """
        return sum([1 for s in S if s in J])