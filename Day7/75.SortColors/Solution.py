class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0]*3
        for i in nums:
            buckets[i]+=1
        i = 0
        for b in range(len(buckets)):
            for c in range(buckets[b]):
                nums[i] = b
                i+=1