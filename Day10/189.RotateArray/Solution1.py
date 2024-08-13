class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        first = nums[0:n-k]
        last = nums[n-k:]
        for i in range(n):
            if i<k:
                nums[i]=last[i]
            else:
                nums[i]=first[i-k]