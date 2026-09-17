func openLock(deadends []string, target string) int {
    deadSet := make(map[string]bool)
    for _, d := range deadends {
        deadSet[d] = true
    }

    if deadSet["0000"] {
        return -1
    }
    if target == "0000" {
        return 0
    }

    visited := map[string]bool{"0000": true}
    queue := []string{"0000"}
    steps := 0

    for len(queue) > 0 {
        steps++
        levelSize := len(queue)
        
        for i := 0; i < levelSize; i++ {
            lock := queue[0]
            queue = queue[1:]

            for pos := 0; pos < 4; pos++ {
                cur := int(lock[pos] - '0')
                for _, delta := range []int{1, -1} {
                    next := (cur + delta + 10) % 10
                    nextLock := lock[:pos] + strconv.Itoa(next) + lock[pos+1:]

                    if deadSet[nextLock] || visited[nextLock] {
                        continue
                    }
                    if nextLock == target {
                        return steps
                    }
                    visited[nextLock] = true
                    queue = append(queue, nextLock)
                }
            }
        }
    }

    return -1
}