class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        for i in range(0,len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1]*nums[i-1])
        k = 0
        i = len(nums)-1
        while i > -1:
            if i ==len(nums)-1:
                postfix.insert(0,1)
                k+=1
            else:
                postfix.insert(0,postfix[0]*nums[i+1])
            i-=1
        print(prefix)
        print(postfix)
        for i in range(0,len(nums)):
            if i ==0:
                nums[i] = postfix[i]
            elif i == len(nums)-1:
                nums[i] = prefix[i]
            else:
                nums[i] = prefix[i]*postfix[i]
        return nums