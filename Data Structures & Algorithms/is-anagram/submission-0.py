class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        list1 = []
        list2 = []
        for i in range(0,len(s)):
            list1.append(s[i])
            list2.append(t[i])
        list1 = set(list1)
        list2 = set(list2)
        if list1.union(list2) == list1 and list2.union(list1) == list2:
            return True
        else:
            return False