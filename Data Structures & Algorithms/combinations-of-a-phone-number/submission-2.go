func letterCombinations(digits string) []string {
	if len(digits) == 0 {
        return []string{}
    }

    res := []string{}
    digitToChar := map[byte]string{
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

	var backtrack func(i int, curStr string)
    backtrack = func(i int, curStr string) {
        if i == len(digits) {
		    res = append(res, curStr)
            return
        }
		
        letters := digitToChar[digits[i]]
        for j := 0; j < len(letters); j++ {
            backtrack(i + 1, curStr+string(letters[j]))
        }
	}

	backtrack(0, "")
	return res
}
