import(
    "fmt"
    "strings"
)

func isAlpha(b byte) bool {
    return ('a' <= b && b <= 'z') || ('A' <= b && b <= 'Z') || ('0' <= b && b <= '9')
}

func isPalindrome(s string) bool {

    s = strings.ToLower(s)
    n := len(s) - 1

    for i, j := 0, n; i < j; i, j = i+1, j-1 {

        for i < j && !isAlpha(s[i]) { i++ }
        for i < j && !isAlpha(s[j]) { j-- }
        if s[i] != s[j] { return false }
    }
    return true
}