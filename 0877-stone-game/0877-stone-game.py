class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice, bob, count = 0, 0, 0
        length = len(piles)

        while length > 0:
            first = piles[0]
            end = piles[-1]

            maximum = max(first, end)
            index = piles.index(maximum)
            piles.pop(index)

            if count % 2 == 0:
                alice += maximum
            else:
                bob += maximum

            length -= 1
        
        return (alice > bob)