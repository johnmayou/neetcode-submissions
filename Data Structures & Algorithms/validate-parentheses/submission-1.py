class Solution:
    def isValid(self, s: str) -> bool:
        pmatching = {')': '(', '}': '{', ']': '['}
        pstack = []
        for ch in s:
            if ch == ')' or ch == '}' or ch == ']':
                if not pstack: return False
                plast = pstack.pop()
                if plast != pmatching[ch]: return False
            else:
                pstack.append(ch)
        return len(pstack) == 0
