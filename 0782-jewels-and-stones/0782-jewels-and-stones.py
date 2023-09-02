class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = collections.Counter(stones)
        cnt = 0

        for j in jewels:
            if j in stones_dict:
                cnt += stones_dict[j]
        
        return cnt