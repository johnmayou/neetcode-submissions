class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        pstack = []
        for ch in s:
            if ch in closeToOpen:
                if pstack and pstack[-1] == closeToOpen[ch]:
                    pstack.pop()
                else:
                    return False
            else:
                pstack.append(ch)
        return len(pstack) == 0