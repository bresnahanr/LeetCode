func isSubsequence(s string, t string) bool {
    var i, j int
    n := len(s)
    m := len(t)

    for i < n && j < m {
        if s[i] == t[j] {
            i++
        }
        j++
    }
    return i == n
}