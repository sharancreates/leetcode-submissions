class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        groups = []
        current = {""}  
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isalpha():
                current = {prefix + char for prefix in current}
                
            elif char == '{':
                stack.append((groups, current))
                groups = []
                current = {""}
                
            elif char == '}':
                inner_result = set().union(*groups, current)
                
                prev_groups, prev_current = stack.pop()
                
                current = {prefix + suffix for prefix in prev_current for suffix in inner_result}
                groups = prev_groups
                
            elif char == ',':
                groups.append(current)
                current = {""}
                
            i += 1
            
        final_set = set().union(*groups, current)
        
        return sorted(list(final_set))
