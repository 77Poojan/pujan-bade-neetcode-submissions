func groupAnagrams(strs []string) [][]string {
	 hashMap := make(map[[26]int][]string)

	for _, word := range(strs) {
		var key [26]int
		for _, ch := range word {
            key[ch-'a']++
        }
		hashMap[key] = append(hashMap[key], word)
	}
	
	println(hashMap)

	result := [][]string{}

	for _, group := range hashMap {
		result = append(result, group)
	}

	return result	
}
