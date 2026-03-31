class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol = [], []
        telepad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i):
            if i == len(digits):
                if sol: res.append("".join(sol[:]))
                return

            for word in telepad[digits[i]]:
                sol.append(word)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res