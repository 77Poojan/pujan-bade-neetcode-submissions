class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            for j in range(len(w1)):
                if j == len(w2):
                    return False

                ch1, ch2 = w1[j], w2[j]
                if order_index[ch1] > order_index[ch2]:
                    return False
                elif order_index[ch1] < order_index[ch2]:
                    break  
        
        return True