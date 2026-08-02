class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        seen = set()
        count = 1
        for i in range(0,len(nums)):
            seen.add(nums[i])
        for i in range(0,len(nums)):
            if nums[i] -1 in seen:
                continue
            else:
                length = 1
                while nums[i]+1 in seen:
                    length+=1
                    nums[i] = nums[i]+1
                count = max(count,length)
        return count