class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        max_count = 0
        
        for i in nums:
            if i-1 not in s:
                count = 1
                while i+count in s:
                    count+=1
                max_count = max(count,max_count)
        return max_count