func generateParenthesis(n int) []string {
    sol := []string {}
    res := []string {}


    var backtrack func(left int, right int) 

    backtrack = func(left int, right int)  {
        if len(sol) == 2 * n {
            res = append(res, strings.Join(sol, ""))
            return
        }

        if left < n {
            sol = append(sol, "(")
            backtrack(left + 1, right)
            sol = sol[:len(sol) - 1]
        }
        
        if right < left {
            sol = append(sol, ")")
            backtrack(left, right + 1)
            sol = sol[:len(sol) - 1]
        }
    }

	backtrack(0, 0)
    return res
}
