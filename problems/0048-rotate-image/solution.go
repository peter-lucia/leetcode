func rotate(matrix [][]int)  {
    // 1. flip across top-left to bottom-right axis 
    // 2. reverse each row
    n := len(matrix)
    m := len(matrix[0])


    for i := 0; i < n; i++ {
        for j := 0; j < i; j++ {
            matrix[i][j], matrix[j][i] = 
              matrix[j][i], matrix[i][j]
        }
    }

   
    for i := 0; i < n; i++ {
        for j := 0; j < m / 2; j++ {
            matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
        }
    }
}
