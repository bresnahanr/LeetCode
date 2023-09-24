func majorityElement(nums []int) int {
    
    n := len(nums)
    m := make(map[int]int)

    for _, val := range nums {
        m[val]++
        if m[val] > n/2 {
            return val
        }
    }
    return -1
}