func decodeString(s string) string {
    stack := []string{}

    for _, ch := range s {
        c := string(ch)

        if c == "]" {
            w := []string{}
            for stack[len(stack)-1] != "[" {
                w = append(w, stack[len(stack)-1])
                stack = stack[:len(stack)-1]
            }

            stack = stack[:len(stack)-1] // pop "["

            num := []string{}
            for len(stack) > 0 && isDigit(stack[len(stack)-1]) {
                num = append(num, stack[len(stack)-1])
                stack = stack[:len(stack)-1]
            }

            reverse(num)
            n, _ := strconv.Atoi(strings.Join(num, ""))

            reverse(w)
            decoded := strings.Repeat(strings.Join(w, ""), n)
            stack = append(stack, decoded)

        } else {
            stack = append(stack, c)
        }
    }

    return strings.Join(stack, "")
}

func isDigit(s string) bool {
    return len(s) == 1 && s[0] >= '0' && s[0] <= '9'
}

func reverse(s []string) {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
}