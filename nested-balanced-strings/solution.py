class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """ ** Stuck **
            Solution approach from hint:
            - Since we care only about the MAX num of balanced strings,
              then we can write a greedy algorithm that adds 1 to our number of
              balanced substrings everytime that we rebalance a substring
            Time complexity: O(n)
        """
        numstrings = 0
        counter = 0
        for c in s:
            if c == 'L':
                counter += 1
            elif c == 'R':
                counter -= 1
            if counter == 0: numstrings += 1

        return numstrings