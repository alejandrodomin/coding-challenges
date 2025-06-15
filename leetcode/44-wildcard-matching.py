class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache
        def match(si: int, pi: int) -> bool:
            if pi == len(p):
                return si == len(s)

            if si == len(s):
                return all(x == "*" for x in p[pi:])

            if s[si] == p[pi] or p[pi] == "?":
                return match(si + 1, pi + 1)

            if p[pi] == "*":
                return match(si + 1, pi) or match(si, pi + 1)

            return False

        return match(0, 0)
