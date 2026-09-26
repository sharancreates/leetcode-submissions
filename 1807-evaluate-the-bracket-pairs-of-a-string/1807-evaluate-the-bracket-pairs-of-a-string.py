class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv_map = {key: val for key, val in knowledge}
        
        result = []
        current_key = []
        in_brackets = False
        
        for char in s:
            if char == '(':
                in_brackets = True
            elif char == ')':
                in_brackets = False
                key_str = "".join(current_key)
                result.append(kv_map.get(key_str, '?'))
                current_key = []
            else:
                if in_brackets:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)
