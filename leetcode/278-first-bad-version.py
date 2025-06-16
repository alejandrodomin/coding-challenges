# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        versions = [None] * n
        visited = []

        search = n // 2

        while search not in visited:
            if isBadVersion(search):
                versions[search - 1] = 1
                search = search // 2
            else:
                versions[search - 1] = 0
                search = ((n - search) // 2) + search

            visited.append(search)

        print(versions)
        return versions.index(1) + 1
