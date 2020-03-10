class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """ Naive solution:
            - Step through list, appending the pairs at each step
            Time complexity: O(n ^ k) where k = freq_1 * ... *freq_n
        """
        #         result = []

        #         for i,num in enumerate(nums[::2]):
        #             result += [nums[i*2 + 1] for x in range(num)]
        #         return result

        """ Optimized Solution 1 (Requires extra knowledge of python operators):
            - Less memory usage (not keeping track of enumeration key,val pairs)
            - Less operations (not slicing array nor iterating over freq range)
        """
        result = []
        for i in range(0, len(nums), 2):
            result += [nums[i + 1]] * nums[i]
        return result