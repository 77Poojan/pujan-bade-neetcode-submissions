func isValid(s string) bool {
	pairs := map[byte]byte{'(': ')', '[': ']', '{': '}'}
	stack := []byte{}

	for i := 0; i < len(s); i++ {
		c := s[i]
		idx := len(stack) - 1

		if idx >= 0 && pairs[stack[idx]] == c {
			stack = stack[:idx]
		} else {
			stack = append(stack, c)
		}
	}

	return len(stack) == 0
}