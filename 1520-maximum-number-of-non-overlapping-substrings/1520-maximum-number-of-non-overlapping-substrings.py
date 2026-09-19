class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in enumerate(s) if c not in s[:i]}
        last = {c: i for i, c in enumerate(s)}
        
        valid_intervals = []
        
        for c in set(s):
            start = first[c]
            end = last[c]
            i = start
            is_valid = True
            
            while i <= end:
                curr_char = s[i]
                if first[curr_char] < start:
                    is_valid = False
                    break
                end = max(end, last[curr_char])
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))
                
        valid_intervals.sort(key=lambda x: (x[1], x[1] - x[0]))
        
        res = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:
                res.append(s[start:end+1])
                prev_end = end
            elif start >= valid_intervals[valid_intervals.index((start, end))-1][0] and end <= prev_end:
                res[-1] = s[start:end+1]
                prev_end = end
                
        return res