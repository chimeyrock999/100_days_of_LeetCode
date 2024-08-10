# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while i <= j:
            m = (i+j)//2
            if isBadVersion(m-1) and isBadVersion(m):
                j = m-1
            elif not isBadVersion(m-1) and not isBadVersion(m):
                i = m+1
            else:
                return m
