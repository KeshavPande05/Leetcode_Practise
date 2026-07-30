class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in sum:
                return [sum[complement], i]
            sum[num] = i