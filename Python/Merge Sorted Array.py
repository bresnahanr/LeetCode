class Solution:
    
    def merge_sorted_array(self, nums1, nums2, m, n ):
        nums1[-n:] = nums2
        nums1.sort()
        return nums1
    
    
sol = Solution()

nums1 = [1,3,5,0,0,0]
nums2 = [2,4,6]
m = 3
n = 3

merged = sol.merge_sorted_array(nums1, nums2, m, n)
print(merged)