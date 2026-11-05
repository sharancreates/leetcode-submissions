class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        output = []
        for i in words:
            output.append(i[::-1])

        return " ".join(output)