class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                num = count[card] 

                for i in range(card, groupSize + card):
                    if count[i] < num:
                        return False
                        
                    count[i] -= num
        return True