from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        count1 = Counter(s)
        count2 = Counter(t)
        for i in range(0,len(s)):
            if count2.get(s[i]) != count1.get(s[i]):
                return False
        return True