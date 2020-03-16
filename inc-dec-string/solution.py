class Solution:
    def sortString(self, s: str) -> str:
        """ Optimized Solution 1:
        - Store all chars in the given string in an alphabetically indexed array in O(n) time
        - Iterate through the alphabet until we've run out of chars, toggling a flag for increasing and decreasing
        """
        alphabets = [0] * 26
        for ch in s:  alphabets[
            ord(ch) - 97] += 1  # takes a one-item array and returns the unicode value of the element

        ans, flag = "", True

        while len(ans) < len(s):
            for i in range(26):
                if flag:
                    pos = i
                else:
                    pos = 25 - i
                if alphabets[pos] is 0: continue
                ans += chr(pos + 97)  # takes a unicode value and returns the corresponding character
                alphabets[pos] -= 1
            flag = not flag

        return ans

        """ Naive Solution:
            - Iterate through the remaining list at each step and go through the steps as written
        """
#         result = []
#         s = sorted(s)

#         while len(s) > 0 :
#             s, result = self.appendIncreasing(s, result)
#             s, result = self.appendDecreasing(s, result)

#         return "".join(result)

#     def appendIncreasing(self, s, result):
#         complete = False
#         ptr = 0
#         first_iter = True

#         while not complete:
#             if (len(s) == 0):
#                 return (s, result)
#             elif first_iter:
#                 smallest = s[ptr]
#                 s.remove(smallest)
#                 result.append(smallest)
#                 first_iter = False
#             else:
#                 found = False
#                 while not found:
#                     if (ptr >= len(s)):
#                         return (s, result)
#                     elif (s[ptr] > result[len(result) - 1]):
#                         larger = s[ptr]
#                         s.remove(larger)
#                         result.append(larger)
#                         found = True
#                     else:
#                         ptr += 1

#         return (s, result)


#     def appendDecreasing(self, s, result):
#         complete = False
#         ptr = len(s) - 1
#         first_iter = True

#         while not complete:
#             if (len(s) == 0):
#                 return (s, result)
#             elif first_iter:
#                 largest = s[ptr]
#                 s.remove(largest)
#                 result.append(largest)
#                 first_iter = False
#                 ptr -= 1
#             else:
#                 found = False
#                 while not found:
#                     if (ptr < 0):
#                         return (s, result)
#                     elif (s[ptr] < result[len(result) - 1]):
#                         smaller = s[ptr]
#                         s.remove(smaller)
#                         result.append(smaller)
#                         found = True
#                     ptr -= 1

#         return (s, result)

