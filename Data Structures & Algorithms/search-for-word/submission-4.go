func exist(board [][]byte, word string) bool {
    m := len(board)
    n := len(board[0])
    dirs := [][2]int {
        {0, 1},
        {0, -1},
        {1, 0},
        {-1, 0},
    }
    
    var backtrack func(i int, j int, k int) bool
    backtrack = func(i int, j int, k int) bool {  
        if k == len(word) {
            return true
        }  

        if i < 0 || j < 0 || i >= m || j >= n {
            return false
        }

        if board[i][j] == '#' || word[k] != board[i][j] {
            return false
        }

        tmp :=  board[i][j]
        board[i][j] = '#'

        for _, d := range dirs {
            if backtrack(d[0] + i, d[1] + j, k + 1) {
                board[i][j] = tmp
                return true
            }
        }

        board[i][j] = tmp
        return false
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if backtrack(i, j, 0) {
                return true
            }
        }
    }

    return false
}
