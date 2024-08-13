class Solution:
    def canReach(self, curr, nums, mark_can_not_reach):
        if mark_can_not_reach[curr]:
            return False
        if curr+nums[curr]>=len(nums)-1:
            return True
        # print(nums[curr])
        i=1
        while i<=nums[curr]:
            if self.canReach(curr+i, nums, mark_can_not_reach):
                return True
            i+=1
        mark_can_not_reach[curr] = True
        return False

    def canJump(self, nums: List[int]) -> bool:
        mark_can_not_reach = [False]*len(nums)
        return self.canReach(0, nums, mark_can_not_reach)
