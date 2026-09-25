class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        
        def check_duplicate(lst:list):
            for i in range(1,len(lst)):
                if lst[i]-lst[i-1]<=k:
                    return True
            return False
        
        
        for i in range(0,len(nums)):
            dic[nums[i]].append(i)
        
        for i in dic:
            if len(dic[i]) >=2:
                if check_duplicate(dic[i]):
                    return True
        return False