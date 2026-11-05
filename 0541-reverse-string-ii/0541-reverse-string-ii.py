class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chunks = []
        
        for i in range(0, len(s), k):
            chunk = s[i : i + k]
            chunks.append(chunk)
        
        for i in range(0, len(chunks), 2):
            chunks[i] = chunks[i][::-1]
            
        return "".join(chunks)
