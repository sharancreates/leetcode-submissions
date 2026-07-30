class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_one = False
        ended = False

        for ch in s:
            if ch == '1':
                if ended:
                    return False
                seen_one = True
            else:  # ch == '0'
                if seen_one:
                    ended = True

        return True