class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def find(left,right,nums,target):
            if left > right:
                return False
            mid = (left+right)//2
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                return find(left+1,right-1,nums,target)
            if nums[mid] == target:
                return True
            elif nums[left] <=nums[mid]:
                if nums[left] >=target and nums[mid] < target:
                    return find(left,mid-1,nums,target)
                else:
                    return find(mid+1,right,nums,target)
            else:
                if nums[right] >= target and nums[mid] < target:
                    return find(mid+1,right,nums,target)
                else:
                    return find(left,mid-1,nums,target)
        return find(0,len(nums)-1,nums,target)