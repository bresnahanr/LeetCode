func removeElement(nums []int, val int) int {
    
    //sort.Ints(nums)
    count := 0

    for i := 0; i < len(nums); i++ {
        if nums[i] != val {
            nums[count] = nums[i]
            count++
        }
    }

    return count
}