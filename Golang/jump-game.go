func canJump(nums []int) bool {
    farthest := 0
    n := len(nums)

    for i, val := range nums {
        if i + val > farthest {
            farthest = i + nums[i]
        }

        if val == 0 && i < n-1 && i == farthest {
            return false
        }
    }

    return true
}