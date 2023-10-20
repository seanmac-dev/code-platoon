class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1


answer = Solution.searchInsert(Solution, [1, 3, 5, 6, 8, 10], 8)
print(answer)
