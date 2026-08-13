from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        left = 0
        right = len(s1)-1
        s2_count = defaultdict(int)
        s2_count = Counter(s2[left:right+1])
        print(s2_count)
        left+=1
        right+=1
        while right < len(s2):
            s2_count[s2[left-1]] -=1
            s2_count[s2[right]] +=1
            if s2_count == s1_count:
                return True

            left+=1
            right+=1
        return False