func lengthOfLongestSubstring(s string) int {
	chars := make(map[byte]int)

    left := 0
    maxx := 0

    for right := 0; right < len(s); right++ {
        ch := s[right]

        if index, exists := chars[ch]; exists && index >= left {
            left = index + 1
        }

        chars[ch] = right

        maxx = max(maxx, right-left+1)
    }

    return maxx
}