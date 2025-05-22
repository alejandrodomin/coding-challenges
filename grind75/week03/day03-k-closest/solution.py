# very easy problem, such a juxtaposition to the o1-matrix kicking my ass

import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        mapping = []
        for x, y in points:
            dstnc = math.sqrt(x ** 2 + y ** 2)
            mapping.append((dstnc, (x, y)))

        mapping = sorted(mapping, key=lambda x: (x[0]))

        return [coord for _, coord in mapping[:k]]
