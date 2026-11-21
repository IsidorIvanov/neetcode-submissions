class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            check = target - nums[i]
            j = i + 1
            if check in nums[j:]:
                return [i, j + nums[j:].index(check)]