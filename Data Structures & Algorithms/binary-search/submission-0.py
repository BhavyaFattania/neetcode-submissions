def binary_search(l,r,target,nums):
        left = l
        right = r
        if left > right:
            return -1

        mid = (left+right) //2
        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            return binary_search(left, mid-1,target,nums)
        elif nums[mid] < target:
            return binary_search(mid+1,right,target,nums) 
        else:
            return -1
               
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(0,len(nums)-1,target,nums)