class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {')': '(', '}': '{', ']': '['}
        pstack = []
        for ch in s:
            if ch in closedToOpen:
                if not pstack or pstack.pop() != closedToOpen[ch]:
                    return False
            else:
                pstack.append(ch)
        return len(pstack) == 0