class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(left,right,nums,mini):
            if left > right:
                return mini
            mid = (left+right)//2
            mini = min(mini,nums[mid])
            if nums[left] <= nums[mid]:
                mini = min(mini,nums[left])
                return find(mid+1,right,nums,mini)
            else:
                mini = min(mini,nums[mid])
                return find(left,mid-1,nums,mini)
        return find(0,len(nums)-1,nums,nums[0])