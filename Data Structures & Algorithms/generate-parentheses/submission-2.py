class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        def backtrack(left, right):
            if (left + right) == 2 * n:
                res.append("".join(sol[:]))
                return

            if left < n:
                sol.append("(")
                backtrack(left + 1, right)
                sol.pop()

            if left > right:
                sol.append(")")
                backtrack(left, right + 1)
                sol.pop()

        backtrack(0, 0)
        return res