class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """ Potential solution 1:
            - Use a counter to keep track of number of parentheses
        """
        parentheses = 0 
        result = ""
        for c in S:
            if(c == "("):
                parentheses += 1
            
            if(parentheses > 1):
                result += c
            
            if(c == ")"):
                parentheses -= 1
        
        return result
    
        """ Proposed solution:
            - We know that our current substring is non-primitive if we have two open brackets or two close brackets in a row
            - We will iterate through the array and remove one of these brackets whenever we encounter the scenario
            Issues:
            - Doesn't consider primitive strings that are deeply nested
        """
#         last_char = S[0]
#         i = 1
#         while i < len(S) - 1:
#             print(f"S[i]: {S[i]} last_char:{last_char}")
#             if S[i] == last_char:
#                 S = S[:i] + S[i+1:]
#                 last_char = S[i]
#                 print(f"S: {S}\n")
#             else: last_char = S[i]
#             i += 1
        
#         if S[len(S) - 1] == S[len(S) - 2] : S = S[:len(S)-1]
#         return S