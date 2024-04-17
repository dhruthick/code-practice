class Solution:
    '''
    EASY: 771
    You're given strings jewels representing the types of stones that
    are jewels, and stones representing the stones you have. Each 
    character in stones is a type of stone you have. You want to 
    know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different 
    type of stone from "A".
    '''
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        for stone in stones:
            count[stone] += 1
        ans = 0
        for jewel in jewels:
            ans += count[jewel]
        return ans