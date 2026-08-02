
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0,len(nums)):
            dict1.update({nums[i]:i})
        print(dict1)
        for i in range(0,len(nums)):
            find = target-nums[i]
            if dict1.get(find) is not None and dict1.get(find) !=i:
                return [i,dict1.get(find)]
        return [0,0]
        