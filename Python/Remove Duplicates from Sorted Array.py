class Solution:

    def remove_duplicates_from_sorted(self, nums):
        index = 0

        for i in nums:
            if nums[index] != i:
                index += 1
                nums[index] = i
        return index
    
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
ans = sol.remove_duplicates_from_sorted(nums)
print(ans)