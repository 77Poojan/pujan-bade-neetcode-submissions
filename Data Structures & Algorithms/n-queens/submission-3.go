func solveNQueens(n int) [][]string {
	col := make([]bool, n)
    posDiag := make([]bool, 2*n)
    negDiag := make([]bool, 2*n)

    var res [][]string
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
            solution := make([]string, n)
            for i := range board {
                solution[i] = string(board[i])
            }
            res = append(res, solution)
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
