class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                if b//a < 0:
                    stack.append(0)
                else:
                    stack.append(b//a)
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()
                            