class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        
        # Start from largest side and check if it can form a polygon
        # A polygon can be formed if the longest side < sum of all other sides
        for i in range(len(nums) - 1, 1, -1):
            total_except_largest = total - nums[i]
            if nums[i] < total_except_largest:
                return total
            total = total_except_largest
        
        return -1