class Solution:
    def toLowerCase(self, str: str) -> str:
        """ Naive solution:
            - Use list comprehension with unicode values, checking if a string is uppercase or lowercase at each step
        """
        return "".join([chr(ord(ch) + 32) if 'A' <= ch <= 'Z' else ch for ch in str])
