class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in matching.values():  
                stack.append(char)
            else:  
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()

        return not stack
