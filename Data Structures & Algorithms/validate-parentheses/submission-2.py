class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in s:
            if i in ("{","[","("):
                stack.append(i)
                print(stack)
            else:
                if i =="]" and stack[-1] != "[":
                    return False
                elif i ==")" and stack[-1] !="(":
                    return False
                elif i =="}" and stack[-1] != "{":
                    return False
                else: stack.pop()
        
        if len(stack) ==0:
            return True
        else:
            return False

