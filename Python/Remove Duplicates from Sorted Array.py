class Solution:

    #Each unique element can appear at most once
    def remove_duplicates_from_sorted(self, nums):
        index = 0

        for i in nums:
            if nums[index] != i:
                index += 1
                nums[index] = i
        return index
    
    #Each unique element can appear at most twice
    def remove_duplicates_from_sorted2(self, nums):

        k = 2

        for i in range( 2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k
    
    
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
ans1 = sol.remove_duplicates_from_sorted(nums)
ans2 = sol.remove_duplicates_from_sorted2(nums)
print(ans1)
print(ans2)