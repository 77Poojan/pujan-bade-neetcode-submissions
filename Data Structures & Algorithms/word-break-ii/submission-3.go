func wordBreak(s string, wordDict []string) []string {
    wordSet := make(map[string]bool)
    for _, word := range wordDict {
        wordSet[word] = true
    }

    sol := []string {}
    res := []string {}
    var backtrack func(i int) 

    backtrack = func(i int) {
        if i == len(s) {
            res = append(res, strings.Join(sol, " "))
            return
        }
        for j:=i; j < len(s); j++ {
            w := s[i : j+ 1]

            if wordSet[w] {
                sol = append(sol, w)
                backtrack(j + 1)
                sol = sol[:len(sol)-1]
            }
        }
    }

    backtrack(0)
    return res
}
