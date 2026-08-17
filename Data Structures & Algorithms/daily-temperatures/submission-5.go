type entry struct {
    index int
    temp  int
}

func dailyTemperatures(temperatures []int) []int {
    dp := make([]int, len(temperatures))
    if len(temperatures) == 0 {
        return dp
    }

    stack := []entry{}
    stack = append(stack, entry{0, temperatures[0]})

    for idx, temperature := range temperatures[1:] {
        idx += 1

        for len(stack) > 0 {
            last := stack[len(stack)-1]
            i, currTemp := last.index, last.temp

            if currTemp >= temperature {
                break
            }
            dp[i] = idx - i
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, entry{idx, temperature})
    }

    return dp
}