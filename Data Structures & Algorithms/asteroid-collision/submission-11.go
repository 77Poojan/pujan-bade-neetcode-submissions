func asteroidCollision(asteroids []int) []int {
    stack := []int{}

    for _, asteroid := range asteroids {
        alive := true

        for len(stack) > 0 && 
            stack[len(stack)-1] > 0 && 
            asteroid < 0 && 
            alive {
            top := stack[len(stack) - 1]

            if top == -asteroid {
                stack = stack[:len(stack) - 1]
                alive = false
            } else if top < -asteroid {
                stack = stack[:len(stack) - 1]
            } else {
				alive = false
			}
        }

        if alive {
			stack = append(stack, asteroid)
		}
    }
    
    return stack
}
