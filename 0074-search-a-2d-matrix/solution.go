func searchMatrix(matrix [][]int, target int) bool {

    n := len(matrix)
    m := len(matrix[0])

    // binary search for row
    // binary search possible row for num

    rowLow := 0
    rowHigh := n - 1
    midRow := -1

    for ;rowLow <= rowHigh; {
        midRow = int(rowLow + ((rowHigh - rowLow) / 2))
        valMidRowMin := matrix[midRow][0]
        valMidRowHigh := matrix[midRow][m-1]
        if valMidRowMin <= target && target <= valMidRowHigh {
            break
        } else if target > valMidRowHigh {
            rowLow = midRow + 1
        } else if target < valMidRowMin {
            rowHigh = midRow - 1
        }
    }

    if midRow == -1 {
        // fmt.Println("midRow is -1")
        return false
    }

    // binary search midRow for num (upgrade to later)
    low := 0
    high := m - 1
    for ;low <= high; {
        mid := int(low + ((high-low) / 2))
        // fmt.Println("Checking ", midRow, mid, matrix)
        val := matrix[midRow][mid]
        if target < val {
            high = mid - 1
        } else if target > val {
            low = mid + 1
        } else {
            return true
        }

    }
    return false
    
}
