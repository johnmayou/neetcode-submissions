class Solution:

    DELIM = "|"

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + self.DELIM + s for s in strs)

    def decode(self, s: str) -> List[str]:
        out: list[str] = []
        i = 0
        while i < len(s):
            delim = i
            while s[delim] != self.DELIM:
                delim += 1
            s_start = delim + 1
            s_end = s_start + int(s[i: delim]) - 1
            out.append(s[s_start: s_end + 1])
            i = s_end + 1
        return out