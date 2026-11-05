func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var dp [26]int

    for i := 0; i < len(s); i++ {
        dp[s[i] - 'a']++
        dp[t[i] - 'a']--
    }

	for _, count := range(dp) {
		if count != 0 {
			return false
		}	
	}
 
	return true
}