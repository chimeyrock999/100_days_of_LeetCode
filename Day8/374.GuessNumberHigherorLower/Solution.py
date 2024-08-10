# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            g = (low + high) // 2
            if guess(g) == 0:
                return g
            elif guess(g) == -1:
                high = g - 1
            else:
                low = g + 1