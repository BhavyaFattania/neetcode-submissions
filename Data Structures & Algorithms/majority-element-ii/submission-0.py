class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        ans = set()
        n = len(nums)
        for i in nums:
            dic[i]+=1 
            if dic[i]>n//3:
                ans.add(i)

        return list(ans)