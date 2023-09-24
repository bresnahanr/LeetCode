func lengthOfLastWord(s string) int {
    
    count := 0

    for i := len(s) - 1; i >= 0; i-- {
        if count== 0 && s[i] == ' ' {
            continue
        }


        if s[i] == ' ' {
            break
        }
        count++
    }
    return count
}