from typing import List

class Solution:
    def calTimeToEat(self, piles: List[int], speed: int) -> int:
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return 0
    
def main():
    print('123')
    exc = Solution();
    print(exc.minEatingSpeed([3,6,7,11], 8))


if __name__ == '__main__':
    main()
