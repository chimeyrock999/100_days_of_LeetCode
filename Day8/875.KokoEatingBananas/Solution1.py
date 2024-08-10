class Solution:
    def canBeEat(self, speed, piles, h):
        if speed == 0:
            return False
        for i in piles:
            h -= i//speed + int(i%speed>0)
        if h >= 0:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = sum(piles)
        while min_speed<=max_speed:
            speed = (min_speed+max_speed)//2
            if self.canBeEat(speed, piles, h) and self.canBeEat(speed - 1, piles, h):
                max_speed = speed - 1
            elif (not self.canBeEat(speed, piles, h)) and (not self.canBeEat(speed - 1, piles, h)):
                min_speed = speed + 1
            else:
                return speed