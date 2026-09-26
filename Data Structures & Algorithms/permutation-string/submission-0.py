class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        want = defaultdict(int)
        for ch in s1:
            want[ch] += 1

        window = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            window[s2[r]] += 1
            if (r - l) + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            if window == want:
                return True

        return False