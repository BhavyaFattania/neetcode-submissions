class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left=0
        right=0
        max_length = 0
        for r in range(0,len(s)):
            dic[s[r]]= 1+dic.get(s[r],0)
            
            while (r-left+1) - max(dic.values()) > k:
                dic[s[left]]-=1
                left+=1
            max_length = max(max_length,r-left+1)
        return max_length
            