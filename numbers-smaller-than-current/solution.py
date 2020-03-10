class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """Trivial solution is O(n^2)"""

        """O(nlogn) solution involves using dictionaries and pre-sorting"""
        if nums is None:
            return []

        sortedArray = nums.copy()
        sortedArray.sort()
        resultsSoFar = {}

        for i, num in enumerate(sortedArray):
            if num not in resultsSoFar:
                resultsSoFar[num] = i

        for i, num in enumerate(nums):
            nums[i] = resultsSoFar[num]

        return nums
