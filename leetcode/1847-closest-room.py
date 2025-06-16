class Solution:
    def closestRoom(
        self, rooms: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        answer = []

        for pref, minSize in queries:
            minDiff = float("inf")
            bestId = -1
            for roomId, size in rooms:
                if size >= minSize:
                    newDiff = abs(roomId - pref)

                    if newDiff < minDiff:
                        bestId = roomId
                        minDiff = newDiff

            answer.append(bestId)

        return answer
