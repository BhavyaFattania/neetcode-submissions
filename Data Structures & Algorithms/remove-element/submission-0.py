class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        while i < len(nums):
            if nums[i] == val:
                print("before popping", nums[i])
                nums.pop(i)
                
            else:
                k+=1
                i+=1
        print(k)
        return k