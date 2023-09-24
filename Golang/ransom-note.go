func canConstruct(ransomNote string, magazine string) bool {
    charMap := make(map[rune]int)

    for _, c := range magazine {
        charMap[c]++
    }

    for _, c := range ransomNote {
        charMap[c] -= 1

        if charMap[c] == -1 {
            return false
        }
    }

    return true
}