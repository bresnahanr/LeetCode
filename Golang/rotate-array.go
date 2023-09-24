func rotate(nums []int, k int)  {
    n := len(nums)
    k %= n

    result := append(nums[n-k:], nums[:n-k]...)
    for i := 0; i <len(nums)

}