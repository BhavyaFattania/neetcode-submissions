class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left,right,nums,target):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= target:
                return find(left,mid-1,nums,target)
            else:
                return find(mid+1,right,nums,target) 

        return find(0,len(nums)-1,nums,target)