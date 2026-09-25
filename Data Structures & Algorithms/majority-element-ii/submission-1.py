class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
            
            if len(dic) > 2:
                new_dic = defaultdict(int)
                for j in dic:
                    if dic[j]>1:
                        new_dic[j] = dic[j]-1
                dic = new_dic
        res = []
        for i in dic.keys():
            if nums.count(i) > len(nums)//3:
                res.append(i)
        return res 

            
                        
        
            