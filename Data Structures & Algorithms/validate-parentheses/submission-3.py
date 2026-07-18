class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []

        for char in s:
            if stack:
                top = stack[-1]
                if char == "}" and top == "{":
                    stack.pop()
                elif char == "]" and top == "[":
                    stack.pop()
                elif char == ")" and top == "(":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        if stack:
            return False
        return True