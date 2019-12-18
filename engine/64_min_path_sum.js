var minPathSum = function (grid) {

    let m = grid.length
    let n = grid[0].length
    let table = new Array(m).fill().map(el => new Array(n).fill(Infinity))
    table[0][0] = grid[0][0]
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (j < n - 1) {
                // take the min of what it is now OR how we can get there from an adjacent tile
                table[i][j + 1] = Math.min(table[i][j + 1], table[i][j] + grid[i][j + 1])
            }
            if (i < m - 1) {
                table[i + 1][j] = Math.min(table[i + 1][j], table[i][j] + grid[i + 1][j])
            }

        }
    }
    return table[m - 1][n - 1]
}