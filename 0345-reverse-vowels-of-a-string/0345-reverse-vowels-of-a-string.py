class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        v = []
        for char in s:
            if char in vowels:
                v.append(char)

        v.reverse()

        s_list = list(s)
        
        v_index = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = v[v_index]
                v_index += 1

        return "".join(s_list)
