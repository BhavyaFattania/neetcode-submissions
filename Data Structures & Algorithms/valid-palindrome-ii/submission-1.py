class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l:str,r:str) -> bool:
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1

            return True


        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                left_s = isPalindrome(left+1,right)
                right_s = isPalindrome(left,right-1)
                return left_s or right_s
            left+=1
            right-=1
        return True

