class Solution:

    def majority_element1(self, nums):

        n = len(nums)
        nums.sort()
        return nums[n//2]
    
    def majority_element2(self, nums):
        n = len(nums)
        m = {}

        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        for key, value in m.items():
            if value > n//2:
                return key
        
        return ()
    
nums = [2,2,1,1,1,2,2]

sol = Solution()
ans1 = sol.majority_element1(nums)
ans2 = sol.majority_element2(nums)
print(ans1)
print(ans2)