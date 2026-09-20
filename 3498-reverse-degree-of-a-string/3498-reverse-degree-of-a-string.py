class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for index, char in enumerate(s, start=1):
            char_value = 26 - (ord(char) - ord('a'))
            total_degree += char_value * index
        return total_degree
