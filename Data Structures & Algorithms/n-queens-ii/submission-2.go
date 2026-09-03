func totalNQueens(n int) int {
	col := make([]bool, n)
    posDiag := make([]bool, 2*n)
    negDiag := make([]bool, 2*n)

    res := 0
    board := make([][]rune, n)

    for i := range board {
        board[i] = make([]rune, n)
        for j := range board[i] {
            board[i][j] = '.'
        }
    }
	
	var backtrack func(r int)
 	backtrack = func(r int){
		if r == n {
            res += 1
            return
        }

		for c := 0; c < n; c++ {
            if col[c] || posDiag[r+c] || negDiag[r-c+n] {
                continue
            }
			
			col[c] = true
            posDiag[r+c] = true
            negDiag[r-c+n] = true
            board[r][c] = 'Q'
			
			backtrack(r + 1)

			col[c] = false
            posDiag[r+c] = false
            negDiag[r-c+n] = false
			board[r][c] = '.'
		}
	}

	backtrack(0)
	return res
}
