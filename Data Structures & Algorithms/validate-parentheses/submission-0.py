class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] =="(" or s[i] =="{" or s[i] =="[":
                stack.append(s[i])
            elif s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
            elif s[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
            elif s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
        if len(stack) ==0:
            return True
        return False
            