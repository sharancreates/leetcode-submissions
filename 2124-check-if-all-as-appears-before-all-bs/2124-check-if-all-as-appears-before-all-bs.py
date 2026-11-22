class Solution:
    def checkString(self, s: str) -> bool:
        index = len(s)
        for i in range(len(s)):
            if s[i] == 'b':
                index = i
                break
        for i in range(index, len(s)):
            if s[i] == 'a':
                return False
        return True

