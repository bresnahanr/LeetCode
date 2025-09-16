class Solution:

    def rotate1(self, nums, k):

        n = len(nums)
        k %= n

        def reverse(left, right):
            while(left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

                
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return nums

    def rotate2(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

sol = Solution()
nums = [0,1,7,2,6,5,2,5]
print(nums)
ans1 = sol.rotate1(nums, 5)
print(ans1)
ans2 = sol.rotate2(nums, 3)
print(ans2)
