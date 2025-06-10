class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)) or (len(s1) == 0 and len(s2) == 0):
            return False

        winSize = len(s1)

        for index in range(len(s2) - winSize + 1):
            if sorted(s1) == sorted(s2[index:index + winSize]):
                return True

        return False

