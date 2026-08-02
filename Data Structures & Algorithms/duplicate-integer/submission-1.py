class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(0,len(nums)):
            if dict.get(nums[i]) is not None:
                return True
            else:
                dict.update({nums[i]:i})
        return False


