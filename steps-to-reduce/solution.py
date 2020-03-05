from math import gcd, floor, log2, pow

class Solution:
    def numberOfSteps(self, num: int) -> int:

        if (num == 0): return 0
        if (num == 1): return 1

        steps = 0
        numCopy = num

        while (numCopy > 1):
            maxPowerOfTwo = int(log2(gcd(int(numCopy), int(pow(2, floor(
                log2(numCopy)))))))  # Take the base-2 log of the largestPowerOfTwo that we can divide from our number
            numCopy /= pow(2, maxPowerOfTwo)
            numCopy -= 1  # We will always have an odd number after the above operation

            steps += maxPowerOfTwo + 1

        return steps