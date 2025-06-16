class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        result = True
        cases = {}
        for equ in equations:
            a, b = equ[0], equ[3]

            if a not in cases:
                cases[a] = True
            if b not in cases:
                cases[b] = True

            if equ[1] == "!":
                result = result and (cases[a] and not cases[b])
            else:
                result = result and (cases[a] and cases[b])

        return result
