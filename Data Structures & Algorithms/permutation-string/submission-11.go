func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) {
        return false
    }

    var dp1, dp2 [26]int // arrays, not slices -> comparable with ==

    for i := 0; i < len(s1); i++ {
        dp1[s1[i]-'a']++
        dp2[s2[i]-'a']++
    }

    if dp1 == dp2 {
        return true
    }

    for j := len(s1); j < len(s2); j++ {
        dp2[s2[j]-'a']++
        dp2[s2[j-len(s1)]-'a']--

        if dp1 == dp2 {
            return true
        }
    }

    return false
}