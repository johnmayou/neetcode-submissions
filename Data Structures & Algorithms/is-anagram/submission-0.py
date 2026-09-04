class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        if len(s) != len(t): return False

        s_chs = {}
        t_chs = {}

        for i in range(len(s)):
            s_chs[s[i]] = s_chs.get(s[i], 0) + 1
            t_chs[t[i]] = t_chs.get(t[i], 0) + 1

        return s_chs == t_chs
