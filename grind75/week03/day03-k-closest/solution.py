# very easy problem, such a juxtaposition to the o1-matrix kicking my ass
# most pythonista solution submitted by someone else
# class Solution(object):
#     def kClosest(self, points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         points.sort(key = lambda x : x[0] ** 2 + x[1] ** 2)
#
#         return points[:k]

# my simplification on their solution

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda x : x[0] ** 2 + x[1] ** 2)[:k]