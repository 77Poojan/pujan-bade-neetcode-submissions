class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = 0, 0
        res, sol = [], []

        def backtrack(left, right, sol):
            if left == right == n:
                res.append("".join(sol[:]))
                return

            if left < n:
                sol.append("(")
                backtrack(left + 1, right,  sol)
                sol.pop()

            if left > right:
                sol.append(")")
                backtrack(left, right + 1,  sol)
                sol.pop()
            
            return

        backtrack(left, right, sol)
        return res