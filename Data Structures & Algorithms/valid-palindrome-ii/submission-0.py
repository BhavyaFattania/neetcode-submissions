class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left< right:
            if s[left] !=s[right]:
                left_s = s[left:right]
                right_s = s[left+1:right+1]
                return left_s == left_s[::-1] or right_s[::-1] == right_s
            
            left+=1
            right-=1
        return True