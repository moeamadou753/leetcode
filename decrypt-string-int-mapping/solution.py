class Solution:
    def freqAlphabets(self, s: str) -> str:
        """ Naive Solution:
            Time complexity: O(n^2)
        """
        ptr = 0
        while ptr < len(s) - 2:
                if s[ptr+2] == "#":
                    s = s[:ptr] + chr(ord('j') + int(s[ptr:ptr+2]) - 10) + (s[-(len(s) - ptr - 3):] if ptr < len(s) - 3 else "")
                else:
                    s = s[:ptr] + chr(ord('a') + int(s[ptr]) - 1) + s[-(len(s) - ptr - 1):]
                ptr += 1
                
        while ptr < len(s):
            s = s[:ptr] + chr(ord('a') + int(s[ptr]) - 1) + (s[-(len(s) - ptr - 1):]  if ptr < len(s) - 1 else "")
            ptr += 1
        return s