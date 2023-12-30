func UniqueChars(substr string, prevResult map[string]bool) bool {
    _, found := prevResult[substr]
    if found {
        return prevResult[substr]
    }
    uniqueChars := map[rune]bool{}
    for _, e := range substr {
        _, found := uniqueChars[e]
        if found {
            // fmt.Println("Unique Chars False for ", substr)
            // memoize
            prevResult[substr] = false
            return false
        } else {
            uniqueChars[e] = true
        }
    }
    // fmt.Println("Unique Chars: True for ", substr)
    // memoize
    prevResult[substr] = true
    return true
}

func Max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func lengthOfLongestSubstring(s string) int {
    // two pointers
    // when two of any characters are in the substring
    // increment the left pointer
    // otherwise
    // increment the right pointer
    if len(s) == 0 {
        return 0
    }

    maxSize := 0
    left := 0
    right := 0
    n := len(s)
    prevResult := map[string]bool{}

    for left < n {
        if left == right {
            right++
            continue
        }
        if right <= n && UniqueChars(s[left:right], prevResult) {
            right++
        } else {
            left++
        }
        maxSize = Max(maxSize, right - left - 1)

    }
    return maxSize
    
}
