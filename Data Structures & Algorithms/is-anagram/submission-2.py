from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        count1 = Counter(s)
        for i in range(0,len(t)):
            if count1.get(t[i]) is None:
                return False
            if count1.get(t[i]) ==0:
                return False
            elif count1.get(t[i]) > 0:
                count1[t[i]] -=1
            
        return True
        