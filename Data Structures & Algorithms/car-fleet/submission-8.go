type entry struct {
    position int
    speed    int
}

func carFleet(target int, position []int, speed []int) int {
    pairs := make([]entry, len(position))

    for i := range position {
        pairs[i] = entry{position[i], speed[i]}
    }

    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i].position > pairs[j].position // descending
    })

    stack := []float64{}

    for _, pair := range pairs {
        time := float64(target-pair.position) / float64(pair.speed)
        stack = append(stack, time)

        if len(stack) >= 2 && stack[len(stack)-1] <= stack[len(stack)-2] {
            stack = stack[:len(stack)-1] // merges into fleet ahead, pop
        }
    }

    return len(stack)
}