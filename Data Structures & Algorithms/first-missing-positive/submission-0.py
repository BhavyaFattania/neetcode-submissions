class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        smallest_pos = 1
        while smallest_pos in s:
            smallest_pos +=1
        return smallest_pos