func IsPalindrome(s string) bool {
	// Convert to runes to correctly handle multi-byte Unicode characters
	runes := []rune(s)
	left := 0
	right := len(runes) - 1

	for left < right {
		if runes[left] != runes[right] {
			return false
		}
		left++
		right--
	}

	return true
}


func partition(s string) [][]string {
	sol := []string {}
	res := [][]string {}

	var backtrack func(i int) 

	backtrack = func(i int) {
        if i == len(s) {
            res = append(res, append([]string{}, sol...))
            return
        }

		for j := i; j < len(s); j++ {
            sub := s[i : j + 1]
			if IsPalindrome(sub) {
                sol = append(sol, sub)
                backtrack(j + 1)
                sol = sol[:len(sol) - 1]
            }
		}
	}

	backtrack(0)
	return res
}
