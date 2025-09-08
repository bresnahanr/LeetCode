class Solution:

    def remove_element(self, nums, val):
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
                
        return index
    
nums = [3,2,2,3]
val = 3

sol = Solution()
count = sol.remove_element(nums, val)
print("Count: ", count, "\nArray: ", nums[:count])

            